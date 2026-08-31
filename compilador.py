import re as regex

#Identificador de variables
identificador = r"^[a-zA-Z]{1}[a-z_A-Z.0-9]*$" #Aun no puedo empezar una variable con . y seguido una letra.

#Tipos de datos
    #double
num = r"^[0-9]+(\.[0-9]+)?$" #No recibe valores negativos, por ahora

    #string
cadena = r'^"[^"]*"$' #Se cambió las comillas dobles habituales por comillas simples

#Expresiones aritmeticas
suma = r"\+"
resta = r"\-"
multi = r"\*"
division = r"\/"

#Corchetes
p_inicial = r"\("
p_final = r"\)"

#Operador de asignacion
op_asignacion = r"\<\-|="
#Simbolos de comparacion
op_comparacion = r"<=|>=|!=|==|<|>"

#Operadores logicos
op_logico = r"\|\||\&\&"

#Palabras reservadas
pa_reservada = r"if|for|in|funtion"

#Contenedores - Arreglos 
contenedor = r"^c$"

coma = r"^,$"

#Comentarios
comentario = r"#[^\n\r]*"

#----------------------------------------------------------------------------------------------------------------------------
texto = "#hola"
resultado = regex.findall(comentario, texto)

print(resultado)
#with open("compi.txt", "r") as archivo:
 #   for linea in archivo:
   #     print(linea.strip())

