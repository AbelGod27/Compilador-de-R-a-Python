# Prueba larga: programa valido que usa todo el subconjunto soportado
# Resultado esperado: Analisis sintactico completado sin errores

# ---------- Variables simples ----------
nombre <- "Abel"
apellido = "Pineda"
edad <- 20
precio <- 25.50
descuento <- -5
temperatura = -12.5
copia <- edad
negativo <- -edad

# ---------- Contenedores y accesos ----------
numeros <- c(1, 2, 3, 4, 5)
nombres <- c("Abel", "Vanya", "Luis")
vacio <- c()
primero <- numeros[1]
segundo = nombres[2]
indice <- 3
tercero <- numeros[indice]
opuesto <- -numeros[2]

# ---------- Expresiones aritmeticas ----------
resultado <- edad + 10
total <- precio * 2
promedio <- total / 2
diferencia <- edad - descuento
mezcla <- -edad + precio * 2 - numeros[3] / 4
n <- length(numeros)
print(resultado)
print()

# ---------- Funciones propias ----------
sumar <- function(a, b) {
  s <- a + b
  return(s)
}

mayor <- function(a, b) {
  if (a > b) {
    return(a)
  } else {
    return(b)
  }
}

cuadrado <- function(x)
return(x * x)

saludo <- function() {
  print("Hola")
}

absoluto <- function(v) {
  if (v < 0)
  return(-v)
  return(v)
}

r1 <- sumar(2, 3)
r2 <- mayor(edad, 18)
r3 <- cuadrado(4)
r4 <- sumar(edad + 1, precio * 2)
r5 <- absoluto(descuento)
saludo()

# ---------- Condicionales ----------
if (edad >= 18) {
  print("Mayor de edad")
} else if (edad >= 13) {
  print("Adolescente")
} else {
  print("Menor de edad")
}

if (precio != 0)
total <- precio * 2
else
total <- 0

if (nombre == "Abel")
{
  print(nombre)
}

# ---------- Ciclos ----------
for (i in numeros) {
  resultado <- resultado + i
}

for (j in c(10, 20, 30))
total <- total + j

for (k in 5)
print(k)

for (nom in nombres) {
  if (nom == "Luis") {
    print(nom)
  }
}

# ---------- Anidacion ----------
contar_mayores <- function(lista, limite) {
  cuenta <- 0
  for (elem in lista) {
    if (elem > limite) {
      cuenta <- cuenta + 1
    } else if (elem == limite) {
      print("Igual al limite")
    }
  }
  return(cuenta)
}

mayores <- contar_mayores(numeros, 2)
print(mayores)

# ---------- Parentesis y asignacion a elementos ----------
area <- (precio + 10) * 2
media <- ((edad + 10) * (precio - 5)) / 2
signo <- -(edad + 1)
envuelto <- (edad)
r6 <- sumar((edad + 1) * 2, 3)
numeros[1] <- 100
numeros[indice] <- edad + 1
numeros[2] <- (precio - 1) * 3
