# Prueba de error de estructura (bloques)
# Cada linea por separado es valida, el error esta en como se combinan
# Resultado esperado: Error sintactico en linea 6: la '{' abierta en esta linea nunca se cierra
# A la funcion le falta su '}' despues del return, asi que todo lo de abajo queda dentro de ella

calcular <- function(lista) {
  total <- 0
  for (elem in lista) {
    if (elem > 2) {
      total <- total + elem
    }
  }
  return(total)

numeros <- c(1, 2, 3, 4, 5)
resultado <- calcular(numeros)
print(resultado)
