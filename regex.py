#Comentarios
COMENTARIO = r"#[^\n\r]*"
#string
CADENA = r'"[^"]*"' #Se cambió las comillas dobles habituales por comillas simples
#Palabras reservadas
PA_RESERVADA = r"\b(?:if|for|in|return|length|function|print)\b" 
#La b es para detectar unicamente palabras completas
#Operador de asignacion
OP_ASIGNACION = r"<-|="
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
NUM = r"-?[0-9]+(?:\.[0-9]+)?"#Se le agrega ?: para que re.findall reciba correctamente strings y no tuplas
#Identificador de variables
IDENTIFICADOR = r"[a-zA-Z_]{1}[a-z_A-Z.0-9]*"



# if\s*\(\s*([a-zA-Z_]{1}[a-zA-Z_0-9]*|[0-9]+)\s*(==|>=|<=|!=|<|>)\s*([a-zA-Z_]{1}[a-zA-Z_0-9]*|[0-9]+)\s*(\s+(\|\||\&\&)\s+([a-zA-Z_]{1}[a-zA-Z_0-9]*|[0-9]+)\s*(==|>=|<=|!=|<|>)\s*([a-zA-Z_]{1}[a-zA-Z_0-9]*|[0-9]+)\s*)?\)\s*
