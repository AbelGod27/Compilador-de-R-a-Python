import re
from regex import *
from lexer import identificar

regex_tokens = (
    f"{COMENTARIO}|{CADENA}|{PA_RESERVADA}|{FUNCIONES_RESERVADAS}|{CONTENEDOR}|{OP_ASIGNACION}|"
    f"{OP_COMPARACION}|{OP_ARITMETICOS}|{P_INICIAL}|{P_FINAL}|"
    f"{COR_INICIAL}|{COR_FINAL}|{LLAVE_INICIAL}|{LLAVE_FINAL}|{COMA}|"
    f"{NUM}|{IDENTIFICADOR}|\\S" #Al leer la línea de codigo, lo que hace es coincidir el texto de izquierda a derecha
    #El \\S es para encontrar los DESCONOCIDO
    #Es importante hacer coincidir
)

def tokenizar(linea):
    if not linea.strip(): #Verifica si una cadena está vacía o no, si lo es, retorna un token vacío
        return []
    tokens = re.findall(regex_tokens, linea)#findall busca coincidencias entre el gerex grande y la linea
    resultado = []
    for texto in tokens:
        if isinstance(texto, str):
            resultado.append(texto)
        elif isinstance(texto, tuple):
            # Tomo el primer elemento no vacío
            valor = next((x for x in texto if x), None)
            if valor:
                resultado.append(valor)
    return resultado

class ErrorLexico(Exception):
    #Se lanza al encontrar un caracter desconocido, detiene la compilacion
    pass

def obtener_tokens(entrada):
    lista = []
    with open(entrada, "r", encoding="utf-8") as doc:
        for num_linea, linea in enumerate(doc, start=1):
            for texto in tokenizar(linea):
                tipo = identificar(texto)
                if tipo == "DESCONOCIDO":
                    raise ErrorLexico(f"Error léxico en línea {num_linea}: carácter desconocido '{texto}'")
                if tipo != "COMENTARIO":          # el parser no los necesita
                    lista.append((tipo, texto, num_linea))
    return lista
