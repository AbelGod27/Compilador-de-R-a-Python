#Tipos de datos
    #double
NUM = r"^-?[0-9]+(\.[0-9]+)?$" #No recibe valores negativos, por ahora

    #string
CADENA = r'^"[^"]*"$' #Se cambió las comillas dobles habituales por comillas simples

#Palabras reservadas
PA_RESERVADA = r"if|for|in|funtion"

#Contenedores - Arreglos 
CONTENEDOR = r"^c$"

#Operador de asignacion
OP_ASIGNACION = r"\<\-|="

#Simbolos de comparacion
OP_COMPARACION = r"<=|>=|!=|==|<|>"

#Operadores logicos
OP_LOGICO = r"\|\||\&\&"

#Expresiones aritmeticas
EXPRESIONES_ARITMETICAS = r"\+|\-|\*|\/"

#Corchetes
P_INICIAL = r"\("
P_FINAL = r"\)"

#Coma
COMA = r"^,$"

#Comentarios
COMENTARIO = r"#[^\n\r]*"

#Identificador de variables
IDENTIFICADOR = r"^[a-zA-Z]{1}[a-z_A-Z.0-9]*$" #Aun no puedo empezar una variable con . y seguido una letra.
