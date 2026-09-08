# Este es un programa de prueba en R

# Asignaciones
x <- 10
y <- 20
mensaje <- "Hola mundo"

# Operaciones aritméticas
resultado <- x + y
diferencia <- y - x
producto <- x * y
division <- y / x

# Contenedor
valores <- c(1, 2, 3, 4, 5)

# Condicional
if (resultado >= 30) {
    print("El resultado es mayor o igual a 30")
} else {
    print("El resultado es menor a 30")
}

# Función definida por el usuario
suma <- function(a, b) {
    return(a + b)
}

# Llamada a la función
total <- suma(x, y)

# Mostrar resultado
print(total)
