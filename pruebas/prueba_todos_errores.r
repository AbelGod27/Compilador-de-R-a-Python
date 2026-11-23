# Prueba con todos los errores que el compilador debe detectar
# Cada caso indica el error esperado en el comentario de arriba
# Nota: el analisis se detiene en el primer error. Los errores lexicos se revisan
# en todo el archivo antes que los sintacticos, asi que se reporta primero el primer error lexico

# ---------- Codigo valido (no debe dar error) ----------
v <- c(1, -2, 3)
x <- -length(v)
y <- .5
print(length(v) + 2)
if (x > 1) { print(x) } else { print(0) }

# ---------- Errores lexicos ----------
# Error lexico: caracter desconocido '''
a <- 'hola'
# Error lexico: caracter desconocido '%'
b <- 5 %% 2
# Error lexico: caracter desconocido '^'
d <- 2 ^ 3
# Error lexico: caracter desconocido '.'
e <- 3.
# Error lexico: caracter desconocido '$'
g <- x$valor
# Error lexico: caracter desconocido ';'
h <- 1; k <- 2
# Error lexico: caracter desconocido '&'
if (x > 1 && y > 2) { print(x) }

# ---------- Errores sintacticos (linea mal formada) ----------
# Operador repetido
total <- x * * 2
# Operacion incompleta
total <- x +
# Falta cerrar un parentesis
print(length(v)
# Doble negativo dentro de c()
w <- c(1, - -2)
# Operacion dentro de un corchete
z <- v[x + 1]
# Condicion sin comparacion
if (x) { print(x) }
# Parametro con valor por defecto
f <- function(p = 1) { return(p) }
# Mas de 3 parentesis anidados
r <- ((((1 + 2))))
# Contenedor dentro de una operacion
s <- c(1, 2) + 1
# Codigo despues de cerrar un bloque en la misma linea
for (i in v) { print(i) } n <- 5
# while no es palabra reservada
while (x > 1) { print(x) }
# Asignacion sin valor
m <-

# ---------- Errores de estructura ----------
# '}' sin una '{' que lo abra
}
# 'else' sin un 'if' antes
else { print(x) }
# 'return' fuera de una funcion
return(x)
# Falta el cuerpo del 'if' (le sigue un else)
if (x > 1)
else
# La '{' abierta nunca se cierra
for (i in v) {
  print(i)
