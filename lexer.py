import re
from regex import *

def identificar(token):
    if re.fullmatch(COMENTARIO, token): 
        return "COMENTARIO"
    elif re.fullmatch(CADENA, token): 
        return "CADENA"
    elif re.fullmatch(PA_RESERVADA, token): 
        return "PALABRA_RESERVADA"
    elif re.fullmatch(CONTENEDOR, token): 
        return "CONTENEDOR"
    elif re.fullmatch(OP_ASIGNACION, token): 
        return "ASIGNACION"
    elif re.fullmatch(OP_COMPARACION, token): 
        return "COMPARACION"
    elif re.fullmatch(EXPRESIONES_ARITMETICAS, token): 
        return "ARITMETICO"
    elif re.fullmatch(P_INICIAL, token): 
        return "PARENTESIS_APERTURA"
    elif re.fullmatch(P_FINAL, token): 
        return "PARENTESIS_CIERRE"
    elif re.fullmatch(COR_INICIAL, token): 
        return "CORCHETE_APERTURA"
    elif re.fullmatch(COR_FINAL, token): 
        return "CORCHETE_CIERRE"
    elif re.fullmatch(LLAVE_INICIAL, token): 
        return "LLAVE_APERTURA"
    elif re.fullmatch(LLAVE_FINAL, token): 
        return "LLAVE_CIERRE"
    elif re.fullmatch(COMA, token): 
        return "COMA"
    elif re.fullmatch(NUM, token): 
        return "NUMERO"
    elif re.fullmatch(IDENTIFICADOR, token): 
        return "IDENTIFICADOR"
    else:
        return "DESCONOCIDO"
