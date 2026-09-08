# Compilador de R a Python

Analizador léxico que tokeniza código escrito en R, identificando y clasificando cada elemento del lenguaje mediante expresiones regulares implementadas en Python.

## ¿De qué trata el proyecto?

El proyecto implementa la fase de **análisis léxico** de un compilador que toma como entrada archivos de código fuente escritos en R y produce un archivo de salida con cada token reconocido junto a su tipo.

El flujo es:
1. Se lee línea por línea el archivo `.r` de entrada.
2. Se aplican expresiones regulares para extraer los tokens.
3. Cada token se clasifica según su tipo (palabra reservada, número, operador, etc.).
4. El resultado se escribe en un archivo `.txt` de salida.

## Estructura del proyecto

```
Compilador-de-R-a-Python/
├── regex.py         # Definición de todas las expresiones regulares
├── lexer.py         # Clasificador de tokens (identifica el tipo de cada token)
├── compilador.py    # Punto de entrada: tokeniza y procesa el archivo de entrada
├── prueba1.txt      # Archivo de prueba de entrada (texto plano)
├── prueba2.r        # Archivo de prueba de entrada (código R)
├── prueba3.r        # Archivo de prueba de entrada
├── prueba4.r        # Archivo de prueba de entrada
├── prueba5.r        # Archivo de prueba de entrada
├── prueba6.r        # Archivo de prueba de entrada
└── prueba_res.txt   # Ejemplo de archivo de salida con tokens clasificados
```

## Tipos de tokens reconocidos

| Tipo                  | Ejemplos                          |
|-----------------------|-----------------------------------|
| `COMENTARIO`          | `# esto es un comentario`         |
| `CADENA`              | `"Hola mundo"`                    |
| `PALABRA_RESERVADA`   | `if`, `for`, `in`, `return`, `function`, `print`, `length` |
| `CONTENEDOR`          | `c(`                              |
| `ASIGNACION`          | `<-`, `=`                         |
| `COMPARACION`         | `==`, `!=`, `<`, `>`, `<=`, `>=`  |
| `ARITMETICO`          | `+`, `-`, `*`, `/`                |
| `PARENTESIS_APERTURA` | `(`                               |
| `PARENTESIS_CIERRE`   | `)`                               |
| `CORCHETE_APERTURA`   | `[`                               |
| `CORCHETE_CIERRE`     | `]`                               |
| `LLAVE_APERTURA`      | `{`                               |
| `LLAVE_CIERRE`        | `}`                               |
| `COMA`                | `,`                               |
| `NUMERO`              | `42`, `3.14`, `-7`                |
| `IDENTIFICADOR`       | `variable`, `miLista`, `x1`       |

## Requisitos

- Python 3.x
- No requiere dependencias externas (solo la librería estándar `re`)

## Uso

```bash
python compilador.py
```

El programa pedirá dos datos:
1. **Archivo de entrada**: ruta al archivo `.r` que deseas analizar.
2. **Archivo de salida**: nombre del archivo `.txt` donde se guardará el resultado.

### Ejemplo de entrada (`codigo.r`)

```r
# Suma dos números
x <- 10
y <- 20
resultado = x + y
print(resultado)
```

### Ejemplo de salida (`resultado.txt`)

```
Línea 1: # Suma dos números
  Token: # Suma dos números → Tipo: COMENTARIO

Línea 2: x <- 10
  Token: x → Tipo: IDENTIFICADOR
  Token: <- → Tipo: ASIGNACION
  Token: 10 → Tipo: NUMERO

Línea 3: y <- 20
  Token: y → Tipo: IDENTIFICADOR
  Token: <- → Tipo: ASIGNACION
  Token: 20 → Tipo: NUMERO
...
```

## Autores

Abel Pineda Godinez
