# Prueba de error lexico y del orden de las fases
# Resultado esperado: Error lexico en linea 16: caracter desconocido '$'
# La linea 12 tiene un error sintactico, pero no se reporta porque
# el analisis lexico revisa todo el archivo antes que el sintactico

x <- 10
y <- 20

suma <- x + y
print(suma)

variable sin_asignacion

lista <- c(x, y)

z <- lista$valor
print(z)
