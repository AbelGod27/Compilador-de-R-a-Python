#Comentarios
COMENTARIO = r"#[^\n\r]*"
#string
CADENA = r'"[^"]*"' #Las comillas simples delimitan el string en Python

#La b es para detectar unicamente palabras completas
#Palabras reservadas
PA_RESERVADA = r"\b(?:if|else|for|in|return|function)\b"
#Funciones reservadas
FUNCIONES_RESERVADAS = r"\b(?:length|print)\b"

#Operador de asignacion
OP_ASIGNACION = r"<-|=(?!=)"
#Simbolos de comparacion
OP_COMPARACION = r"<=|>=|!=|==|<|>"
#Expresiones aritmeticas
EXPRESIONES_ARITMETICAS = r"\+|\-|\*|\/"
#Parentesis
P_INICIAL = r"\("
P_FINAL = r"\)"
#Corchetes
COR_INICIAL = r"\["
COR_FINAL = r"\]"
#Llaves
LLAVE_INICIAL = r"\{"
LLAVE_FINAL = r"\}"
#Coma
COMA = r","
#Contenedores - Arreglos 
CONTENEDOR = r"c\("
#double
NUM = r"[0-9]+(?:\.[0-9]+)?"#Se le agrega ?: para que re.findall reciba correctamente strings y no tuplas
#Identificador de variables
IDENTIFICADOR = r"[a-zA-Z_]{1}[a-z_A-Z.0-9]*"

