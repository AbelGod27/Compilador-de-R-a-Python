import re
from regex import *
from lexer import identificar

regex_espacio = (
    f"{COMENTARIO}|{CADENA}|{PA_RESERVADA}|{CONTENEDOR}|{OP_ASIGNACION}|"
    f"{OP_COMPARACION}|{EXPRESIONES_ARITMETICAS}|{P_INICIAL}|{P_FINAL}|"
    f"{COR_INICIAL}|{COR_FINAL}|{LLAVE_INICIAL}|{LLAVE_FINAL}|{COMA}|"
    f"{NUM}|{IDENTIFICADOR}"
)

def tokenizar(linea):
    if not linea.strip():
        return []
    tokens = re.findall(regex_espacio, linea)
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

def procesar_archivo(entrada, salida):
    with open(entrada, "r", encoding="utf-8") as doc_entrada, open(salida, "w", encoding="utf-8") as doc_salida:
        for num_linea, linea in enumerate(doc_entrada, start=1):
            tokens = tokenizar(linea)
            if tokens: #En caso de no haber tokens, el if no se activa
                doc_salida.write(f"Línea {num_linea}: {linea.strip()}\n")
                for texto in tokens:
                    tipo = identificar(texto)
                    doc_salida.write(f"  Token: {texto} → Tipo: {tipo}\n")
                doc_salida.write("\n")


if __name__ == "__main__":
    entrada = input("Ingrese el nombre del archivo a traspilar: ")
    salida = input("Ingrese el nombre del archivo de salida: ")
    procesar_archivo(entrada, salida)
    print(f"Procesamiento completo. Revisa {salida}")