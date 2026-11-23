# Compilador de R a Python

Compilador por fases que analiza código escrito en un subconjunto de R. Por ahora implementa el **análisis léxico** y el **análisis sintáctico**, ambos con expresiones regulares en Python.

## ¿De qué trata el proyecto?

El compilador recibe un archivo `.r` y lo revisa en fases. Como un compilador real, **se detiene en el primer error** que encuentra y muestra la línea donde ocurrió.

1. **Análisis léxico**: lee el archivo línea por línea, separa cada línea en tokens y clasifica cada token según su tipo (número, identificador, operador, etc.). Si encuentra un carácter desconocido, se detiene con un error léxico.
2. **Análisis sintáctico**: solo empieza si el léxico terminó sin errores. Revisa que cada línea tenga una forma válida y que los bloques (`{ }`, `if`, `else`, `for`, `function`, `return`) estén bien formados.

Las fases van en orden: el léxico revisa **todo** el archivo antes de que empiece el sintáctico. Por eso, si un archivo tiene un error sintáctico en la línea 5 y un error léxico en la línea 10, se reporta el error léxico.

## Estructura del proyecto

```
Compilador-de-R-a-Python/
├── regex.py         # Expresiones regulares de cada tipo de token
├── lexer.py         # Identifica el tipo de cada token
├── compilador.py    # Tokeniza el archivo completo y detecta errores léxicos
├── parser.py        # Análisis sintáctico y punto de entrada del programa
└── pruebas/         # Archivos .r de prueba
```

## Análisis léxico

### Tipos de tokens reconocidos

| Tipo                  | Ejemplos                                     |
|-----------------------|----------------------------------------------|
| `COMENTARIO`          | `# esto es un comentario`                    |
| `CADENA`              | `"Hola mundo"`                               |
| `PALABRA_RESERVADA`   | `if`, `else`, `for`, `in`, `return`, `function` |
| `FUNCION_RESERVADA`   | `print`, `length`                            |
| `CONTENEDOR`          | `c(` (la `c` debe ir pegada al paréntesis)   |
| `ASIGNACION`          | `<-`, `=`                                    |
| `COMPARACION`         | `==`, `!=`, `<`, `>`, `<=`, `>=`             |
| `ARITMETICO`          | `+`, `-`, `*`, `/`                           |
| `PARENTESIS_APERTURA` | `(`                                          |
| `PARENTESIS_CIERRE`   | `)`                                          |
| `CORCHETE_APERTURA`   | `[`                                          |
| `CORCHETE_CIERRE`     | `]`                                          |
| `LLAVE_APERTURA`      | `{`                                          |
| `LLAVE_CIERRE`        | `}`                                          |
| `COMA`                | `,`                                          |
| `NUMERO`              | `42`, `3.14`, `.5`                           |
| `IDENTIFICADOR`       | `variable`, `miLista`, `x1`, `n.val`         |

Cualquier otro carácter (`$`, `ñ`, `&`, `;`, etc.) es `DESCONOCIDO` y produce un error léxico.

Los números negativos se reconocen como dos tokens: el operador `-` y el número. El signo lo interpreta el análisis sintáctico.

## Análisis sintáctico

### Cómo funciona

1. Los tokens de cada línea se convierten en una **firma**: un texto con sus tipos separados por espacios. Por ejemplo, `edad <- 20` produce la firma `IDENTIFICADOR ASIGNACION NUMERO`. Los operadores aritméticos y las palabras reservadas usan su valor (`-`, `if`, `for`…) para poder distinguirlos.
2. Si la línea trae un bloque completo, como `if (x > 1) { print(x) }`, se divide en partes: después de cada `{` y antes de cada `}`. Cada parte se revisa por separado (`} else {` se queda junto).
3. Las llamadas a funciones que están dentro de otra expresión se reducen a un solo valor (`LLAMADA_INTERNA`), empezando por la más interna. Así `print(length(v))` se revisa como `print(valor)`.
4. La firma se compara con los patrones de `TIPOS_LINEA` y la línea recibe el tipo del primer patrón que coincida. Si no coincide con ninguno, es un error sintáctico.
5. Una pila revisa la estructura de los bloques entre líneas.

### Tipos de línea reconocidos

| Tipo                      | Ejemplo                                  |
|---------------------------|------------------------------------------|
| `ASIGNACION_NUM_POSITIVO` | `edad <- 20`                             |
| `ASIGNACION_NUM_NEGATIVO` | `y <- -3`                                |
| `ASIGNACION_CADENA`       | `nombre <- "Abel"`                       |
| `ASIGNACION_VARIABLE`     | `copia <- edad`                          |
| `ASIGNACION_VAR_NEGATIVA` | `negativo <- -edad`, `x <- -length(v)`   |
| `ASIGNACION_ACCESO`       | `primero <- numeros[1]`                  |
| `ASIGNACION_CONTENEDOR`   | `numeros <- c(1, -2, 3)`                 |
| `ASIGNACION_EXPRESION`    | `area <- (precio + 10) * 2`              |
| `ASIGNACION_FUNCION`      | `n <- length(numeros)`, `n <- length(v + 1)` |
| `ASIGNACION_LLAMADA`      | `r <- sumar(2, 3)`                       |
| `ASIGNACION_ELEMENTO`     | `numeros[1] <- 100`                      |
| `DEFINICION_FUNCION`      | `sumar <- function(a, b) {`              |
| `LLAMADA_FUNCION`         | `print(x)`, `print()`, `print(t + 2)`, `print(length(v))` |
| `LLAMADA_PROPIA`          | `sumar(2, 3)`                            |
| `RETORNO`                 | `return(a + b)`, `return()`              |
| `CONDICIONAL_IF`          | `if (edad >= 18) {`, `if (length(v) + 1 > 3) {` |
| `CONDICIONAL_ELSE_IF`     | `} else if (edad >= 13) {`               |
| `CONDICIONAL_ELSE`        | `} else {`                               |
| `CICLO_FOR`               | `for (i in numeros) {`                   |
| `INICIO_BLOQUE`           | `{`                                      |
| `FIN_BLOQUE`              | `}`                                      |

`if`, `else`, `for` y `function` pueden llevar llaves o no. Si no las llevan, su cuerpo es la línea siguiente. Con llaves, el bloque completo también puede ir en una sola línea: `if (x > 1) { print(x) } else { print(0) }`.

Dentro de los paréntesis de `print`, `length`, las llamadas propias, `return` y las condiciones se aceptan operaciones y llamadas anidadas: `print(sumar(1, length(v)) * 2)`.

### Revisión de estructura

Además de la forma de cada línea, se revisa que:

- toda `{` se cierre con su `}`;
- no haya una `}` sin una `{` que la abra;
- `else` y `else if` vayan después de un `if` o `else if`;
- `if`, `else`, `for` y `function` sin llaves tengan una línea de cuerpo;
- `return` esté dentro de una función;
- el archivo tenga código (un archivo vacío o con solo comentarios es un error).

### Subconjunto de R soportado

El compilador trabaja con un subconjunto limitado de R. Lo que no aparece en las tablas anteriores no forma parte del lenguaje, por ejemplo `while`, `&&`, `||`, `TRUE`, `FALSE` y `;`. Además, estos casos se consideran inválidos:

- condiciones sin comparación: `if (x)`;
- operaciones o llamadas dentro de un corchete: `v[i + 1]`, `v[length(v)]`;
- operaciones dentro de `c(...)`: `c(1 + 2, 3)` (los negativos sí se aceptan: `c(1, -2)`);
- código después de cerrar un bloque en la misma línea: `for (i in v) { print(i) } x <- 5`;
- una instrucción repartida en varias líneas;
- más de 3 niveles de paréntesis anidados en una expresión.

## Requisitos

- Python 3.x
- No requiere dependencias externas (solo las librerías estándar `re` y `sys`)

## Uso

```bash
python parser.py
```

El programa pide el nombre del archivo `.r` que quieres analizar, incluyendo la carpeta, por ejemplo `pruebas/prueba_corta.r` (o `pruebas\prueba_corta.r` en Windows). Si el archivo no existe, se muestra:

```
Error: no se encontró el archivo 'prueba/prueba_corta.r'. Revisa que el nombre y la carpeta estén bien escritos
```

### Ejemplo sin errores (`pruebas/prueba_corta.r`)

```r
# Prueba corta: programa valido minimo
x <- 10
y <- -3
total <- x + y
print(total)
```

Salida:

```
Línea 4: ASIGNACION_NUM_POSITIVO | x <- 10
Línea 5: ASIGNACION_NUM_NEGATIVO | y <- - 3
Línea 6: ASIGNACION_EXPRESION | total <- x + y
Línea 7: LLAMADA_FUNCION | print ( total )
Análisis sintáctico completado sin errores
```

### Ejemplos con errores

```
Error léxico en línea 16: carácter desconocido '$'
Error sintáctico en línea 21: 'total <- precio * * 2'
Error sintáctico en línea 6: la '{' abierta en esta línea nunca se cierra
Error sintáctico: el archivo está vacío, no tiene código para analizar
```

## Pruebas

| Archivo                       | Resultado esperado                                         |
|-------------------------------|------------------------------------------------------------|
| `prueba_corta.r`              | Sin errores                                                |
| `prueba_larga.r`              | Sin errores (usa todo el subconjunto soportado)            |
| `prueba_error_mitad.r`        | Error sintáctico en la línea 21                            |
| `prueba_error_lexico.r`       | Error léxico en la línea 16 (aunque la línea 12 tenga un error sintáctico) |
| `prueba_error_estructura.r`   | Error de estructura: una función sin su `}` de cierre      |
| `prueba_todos_errores.r`      | Error léxico en la línea 15 (reúne 24 casos de error)      |

Cada archivo indica en su primer comentario el resultado esperado.

`prueba_todos_errores.r` es un catálogo: cada caso tiene arriba un comentario con el error esperado (léxico, sintáctico o de estructura). Como el análisis se detiene en el primer error, para probar los demás casos hay que comentar o borrar los que ya se reportaron.

## Autores

Abel Pineda Godinez
