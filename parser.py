import re
import sys
from compilador import obtener_tokens, ErrorLexico

class ErrorSintactico(Exception):
    #Se lanza al encontrar una linea que no coincide con ningun tipo, detiene la compilacion
    pass

#Acceso a un elemento: v[1] o v[i]
ACCESO = r"IDENTIFICADOR CORCHETE_APERTURA (?:NUMERO|IDENTIFICADOR) CORCHETE_CIERRE"
#Son los valores que se pueden repetir
VALOR = rf"(?:{ACCESO}|NUMERO|IDENTIFICADOR|CADENA)"
#Termino: un valor o una expresion entre parentesis, por ejemplo a o ( a + b )
#Un regex no puede contar parentesis, por eso se construye por niveles: se aceptan hasta 3 parentesis anidados
TERMINO = VALOR
for _ in range(3):
    GRUPO = rf"PARENTESIS_APERTURA \-? ?{TERMINO}(?: [+\-*/] \-? ?{TERMINO})* PARENTESIS_CIERRE"
    TERMINO = rf"(?:{VALOR}|{GRUPO})"
#Expresion: identifica si existen distintos valores unidos por una operador aritmetico dentro de una asignacion
#Tambien acepta una expresion sola entre parentesis: ( a + b )
EXPR = rf"(?:\-? ?{TERMINO}(?: [+\-*/] \-? ?{TERMINO})+|\-? ?{GRUPO})"
#Contenedor: c(valor, valor, ..., valor_n), el ? al final del grupo permite un contenedor vacío
LISTA = rf"CONTENEDOR(?: {VALOR}(?: COMA {VALOR})*)? PARENTESIS_CIERRE"
#Llave opcional al final de if, else, for y function
ABRE = r"(?: LLAVE_APERTURA)?"
#Condicion: ( valor comparacion valor )
COND = rf"PARENTESIS_APERTURA {VALOR} COMPARACION {VALOR} PARENTESIS_CIERRE"
#Parametros de una funcion: ( ), ( a ), ( a , b )
PARAMS = r"(?: IDENTIFICADOR(?: COMA IDENTIFICADOR)*)?"
#Argumentos de una llamada: ( ), ( 2 ), ( a , b + 1 )
ARG = rf"(?:{EXPR}|\-? ?{VALOR})"
ARGS = rf"(?: {ARG}(?: COMA {ARG})*)?"
#Llamada a una funcion propia: sumar ( 2 , 3 )
LLAMADA = rf"IDENTIFICADOR PARENTESIS_APERTURA{ARGS} PARENTESIS_CIERRE"

#Tipos de linea, se revisan en orden y gana el primero que coincide
TIPOS_LINEA = [
    #Asignaciones
    ("ASIGNACION_NUM_POSITIVO", r"IDENTIFICADOR ASIGNACION NUMERO"), #valor = 12
    ("ASIGNACION_NUM_NEGATIVO", r"IDENTIFICADOR ASIGNACION - NUMERO"), #valor = -12
    ("ASIGNACION_CADENA",       r"IDENTIFICADOR ASIGNACION CADENA"), #valor = "hola"
    ("ASIGNACION_VARIABLE",     r"IDENTIFICADOR ASIGNACION IDENTIFICADOR"), #valor1 = valor2
    ("ASIGNACION_VAR_NEGATIVA", rf"IDENTIFICADOR ASIGNACION - (?:{ACCESO}|IDENTIFICADOR)"), #valor1 = -valor2
    ("ASIGNACION_ACCESO",       rf"IDENTIFICADOR ASIGNACION {ACCESO}"), #valor = valor1[2]
    ("ASIGNACION_CONTENEDOR",   rf"IDENTIFICADOR ASIGNACION {LISTA}"), #valor = c(1,2,3)
    ("ASIGNACION_EXPRESION",    rf"IDENTIFICADOR ASIGNACION {EXPR}"), #resultado <- edad + 10
    ("ASIGNACION_FUNCION",      rf"IDENTIFICADOR ASIGNACION FUNCION_RESERVADA PARENTESIS_APERTURA {VALOR} PARENTESIS_CIERRE"), #n <- length ( v )
    ("ASIGNACION_LLAMADA",      rf"IDENTIFICADOR ASIGNACION {LLAMADA}"), #r <- sumar ( 2 , 3 )
    ("ASIGNACION_ELEMENTO",     rf"{ACCESO} ASIGNACION {ARG}"), #v[1] <- 5
    #Funciones
    ("DEFINICION_FUNCION",      rf"IDENTIFICADOR ASIGNACION function PARENTESIS_APERTURA{PARAMS} PARENTESIS_CIERRE{ABRE}"), #saludo <- function (parametro)
    ("LLAMADA_FUNCION",         rf"FUNCION_RESERVADA PARENTESIS_APERTURA(?: {VALOR})? PARENTESIS_CIERRE"), #print( x ) o print( )
    ("LLAMADA_PROPIA",          LLAMADA), #sumar ( 2 , 3 )
    ("RETORNO",                 rf"return PARENTESIS_APERTURA(?: {ARG})? PARENTESIS_CIERRE"), #return (total)
    #Condicionales
    ("CONDICIONAL_IF",          rf"if {COND}{ABRE}"), #if ( x == 1 )
    ("CONDICIONAL_ELSE_IF",     rf"(?:LLAVE_CIERRE )?else if {COND}{ABRE}"), #} else if ( x < 3 ) {
    ("CONDICIONAL_ELSE",        rf"(?:LLAVE_CIERRE )?else{ABRE}"), #} else {
    #Ciclos
    ("CICLO_FOR",               rf"for PARENTESIS_APERTURA IDENTIFICADOR in (?:{LISTA}|{VALOR}) PARENTESIS_CIERRE{ABRE}"), #for( i in c( 1 , 2 , 3 ) ) o for( i in 5 )
    #Bloques
    ("INICIO_BLOQUE",           r"LLAVE_APERTURA"), #{
    ("FIN_BLOQUE",              r"LLAVE_CIERRE"), #}
]

def firma(tokens):
    #Convierte los tokens de una linea en un texto con sus tipos
    #Los operadores y palabras reservadas usan su valor para distinguir - de + o if de for
    partes = []
    for tipo, valor, _ in tokens:
        if tipo in ("ARITMETICO", "PALABRA_RESERVADA"):
            partes.append(valor)
        else:
            partes.append(tipo)
    return " ".join(partes) #Une las partes en un texto separado por espacios para compararlo con el regex

def clasificar(tokens):
    f = firma(tokens)
    for nombre, patron in TIPOS_LINEA:
        if re.fullmatch(patron, f):
            return nombre
    return "ERROR_SINTACTICO"

def agrupar_por_linea(tokens):
    #Junta los tokens que pertenecen a la misma linea usando su numero de linea
    lineas = {}
    for tok in tokens:
        lineas.setdefault(tok[2], []).append(tok)
    return lineas

#Lineas que pueden tener cuerpo (con llaves o en la linea siguiente)
ENCABEZADOS = {
    "CONDICIONAL_IF":      "if",
    "CONDICIONAL_ELSE_IF": "else if",
    "CONDICIONAL_ELSE":    "else",
    "CICLO_FOR":           "for",
    "DEFINICION_FUNCION":  "function",
}

class Estructura:
    #Está clase revisa que los bloques esten bien formados usando una pila:
    #  - toda { debe cerrarse con su }
    #  - no puede haber } sin una { abierta
    #  - else / else if solo pueden ir despues de un if o else if
    #  - if, else, for y function sin llaves necesitan una linea siguiente como cuerpo
    #  - return solo puede ir dentro de una function
    def __init__(self):
        self.pila = []             #bloques abiertos: (tipo, num_linea, dentro_de_funcion)
        self.pendiente = None      #encabezado sin llave que espera su cuerpo: (tipo, num_linea, dentro_de_funcion)
        self.puede_else = False    #True si lo ultimo que termino fue un if o else if

    def error(self, num_linea, mensaje):
        raise ErrorSintactico(f"Error sintáctico en línea {num_linea}: {mensaje}")

    def dentro_funcion(self):
        #True si la linea actual esta dentro de una function (con o sin llaves)
        if self.pendiente and self.pendiente[2]:
            return True
        return bool(self.pila) and self.pila[-1][2]

    def revisar(self, num_linea, tipo, toks):
        abre = toks[-1][0] == "LLAVE_APERTURA"   #la linea termina en { devuelve un True
        cierra = toks[0][0] == "LLAVE_CIERRE"    #la linea empieza con } devuelve un True

        #Un encabezado sin llave no puede quedarse sin cuerpo
        if self.pendiente and (cierra or tipo in ("CONDICIONAL_ELSE", "CONDICIONAL_ELSE_IF")):
            enc, linea_enc, _ = self.pendiente
            self.error(num_linea, f"falta el cuerpo del '{ENCABEZADOS[enc]}' de la línea {linea_enc}")

        #Cerrar el bloque que este abierto
        if cierra:
            if not self.pila:
                self.error(num_linea, "'}' sin una '{' que lo abra")
            cerrado, _, _ = self.pila.pop()
            self.puede_else = cerrado in ("CONDICIONAL_IF", "CONDICIONAL_ELSE_IF")

        #else / else if solo despues de un if
        if tipo in ("CONDICIONAL_ELSE", "CONDICIONAL_ELSE_IF") and not self.puede_else:
            self.error(num_linea, f"'{ENCABEZADOS[tipo]}' sin un 'if' antes")

        #return solo dentro de una function
        if tipo == "RETORNO" and not self.dentro_funcion():
            self.error(num_linea, "'return' fuera de una función")

        #Si el bloque o encabezado nuevo esta dentro de una function, o es una function
        en_funcion = self.dentro_funcion() or tipo == "DEFINICION_FUNCION"

        if abre:
            #Una { sola despues de un encabezado sin llave pertenece a ese encabezado
            if tipo == "INICIO_BLOQUE" and self.pendiente:
                dueno = self.pendiente[0]
            else:
                dueno = tipo
            self.pila.append((dueno, num_linea, en_funcion))
            self.pendiente = None
            self.puede_else = False
        elif tipo in ENCABEZADOS:
            #Encabezado sin llave: su cuerpo es la linea siguiente
            self.pendiente = (tipo, num_linea, en_funcion)
            self.puede_else = False
        elif self.pendiente:
            #Esta linea es el cuerpo del encabezado pendiente
            self.puede_else = self.pendiente[0] in ("CONDICIONAL_IF", "CONDICIONAL_ELSE_IF")
            self.pendiente = None
        elif not cierra:
            self.puede_else = False

    def terminar(self):
        #Al final del archivo no debe quedar nada abierto
        if self.pendiente:
            enc, linea_enc, _ = self.pendiente
            self.error(linea_enc, f"el '{ENCABEZADOS[enc]}' no tiene cuerpo")
        if self.pila:
            _, linea_abre, _ = self.pila[-1]
            self.error(linea_abre, "la '{' abierta en esta línea nunca se cierra")

def analizar(entrada):
    #Regresa una lista de (num_linea, tipo_linea, tokens)
    resultado = []
    estructura = Estructura()
    for num_linea, toks in agrupar_por_linea(obtener_tokens(entrada)).items():
        tipo = clasificar(toks)
        if tipo == "ERROR_SINTACTICO":
            codigo = " ".join(t[1] for t in toks)
            raise ErrorSintactico(f"Error sintáctico en línea {num_linea}: '{codigo}'")
        estructura.revisar(num_linea, tipo, toks)
        resultado.append((num_linea, tipo, toks))
    estructura.terminar()
    return resultado


if __name__ == "__main__":
    entrada = input("Ingrese el nombre del archivo a analizar: ")
    try:
        resultado = analizar(entrada)
    except (ErrorLexico, ErrorSintactico) as e:
        print(e)
        sys.exit(1)
    for num_linea, tipo, toks in resultado:
        print(f"Línea {num_linea}: {tipo} | {' '.join(t[1] for t in toks)}")
    print("Análisis sintáctico completado sin errores")
