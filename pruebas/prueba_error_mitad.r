# Prueba con un error sintactico a mitad del codigo
# Resultado esperado: Error sintactico en linea 21: 'total <- precio * * 2'
# Las lineas anteriores son validas y las posteriores ya no se revisan

nombre <- "Abel"
edad <- 20
precio <- 25.50
numeros <- c(1, 2, 3, 4, 5)

sumar <- function(a, b) {
  return(a + b)
}

if (edad >= 18) {
  print("Mayor de edad")
} else {
  print("Menor de edad")
}

resultado <- sumar(edad, 10)
total <- precio * * 2
print(total)

for (i in numeros) {
  resultado <- resultado + i
}

print(resultado)
