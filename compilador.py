from lexer import identificar

with open("compi.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(identificar(linea.strip()))
        