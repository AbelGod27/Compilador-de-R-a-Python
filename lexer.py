import re
from regex import (
    NUM,
    CADENA,
    PA_RESERVADA,
    CONTENEDOR,
    OP_ASIGNACION,
    OP_COMPARACION,
    OP_LOGICO,
    EXPRESIONES_ARITMETICAS,
    P_INICIAL,
    P_FINAL,
    COMA,
    COMENTARIO,
    IDENTIFICADOR 
)

def identificar(token):

    if re.fullmatch(NUM, token):
        return "NUMERO"

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
    
    elif re.fullmatch(OP_LOGICO, token):
        return "LOGICO"

    elif re.fullmatch(P_INICIAL, token):
        return "PARENTESIS_APERTURA"

    elif re.fullmatch(P_FINAL, token):
        return "PARENTESIS_CIERRE"

    elif re.fullmatch(COMA, token):
        return "COMA"

    elif re.fullmatch(IDENTIFICADOR, token):
        return "IDENTIFICADOR"

    elif re.fullmatch(COMENTARIO, token):
        return "COMENTARIO"

    return "DESCONOCIDO"