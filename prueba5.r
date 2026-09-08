# inicio del programa de prueba largo

# asignaciones simples
a=10
b=-5
c=a+b
d=c-2
variable sin_asignacion
=mal_inicio

# operaciones aritméticas
x=100
y=x/2
z=y*3
resultado=z-15
operacion_invalida=+   # error: operador sin operandos

# condicionales
if(a>=10)
if(b!=c)
if(d<=0)
if(>=x)   # error: operador sin identificador
if(a=)    # error: falta valor
if(a<10){ print("menor") }
if(a>10){ print("mayor") }

# funciones
suma(x,y)
resta(a,b)
funcion(param1,param2)
funcion(,)   # error: parámetros vacíos
funcion(param1 param2)   # error: falta coma
funcion()   # error: sin parámetros

# contenedores
valores=c(1,2,3,4)
datos=c("uno","dos","tres")
c(,)   # error: contenedor vacío
c(1 2 3)   # error: falta coma
c("a","b","c","d","e","f")

# cadenas
mensaje="Hola mundo"
cadena="Texto sin cierre
cadena2="Texto correcto"
cadena3="12345"
cadena4="con espacios y símbolos !@#"

# estructuras con llaves y corchetes
{ [ ] }
{ [ ] } extra   # error: token inesperado
{ resultado=10 }
[1,2,3,4,5]

# operadores de comparación y asignación
!= == <= >=
<- =

# mezcla de todo
total=valores[2]+suma(a,b)
if(total>50){
    mensaje="Total mayor a 50"
}
else{
    mensaje="Total menor o igual a 50"
}
print(mensaje)

# fin del programa de prueba largo
