"""
1. Imprime "¡Hola Mundo!" por consola.
2. Escribe un comentario de una sola línea explicando qué
hace el código del Ejercicio 1.
3. Imprime tu nombre y edad en la misma línea utilizando la
función print.
4. Usa la función type() para imprimir el tipo de dato de
una cadena de texto, un número entero y un número
decimal.
5. Escribe un comentario en varias líneas explicando qué
son los tipos de datos en Python.
6. Imprime el resultado de concatenar dos cadenas de texto,
por ejemplo: "Hola" y "Mundo".
7. Crea una variable para almacenar tu nombre, otra para tu
edad, e imprime ambas en la misma línea.
8. Escribe un programa que solicite al usuario su nombre y
lo imprima junto con un saludo.
9. Usa print() para mostrar el resultado de la suma de dos
números enteros y el tipo de dato resultante.
10. Comenta el código del Ejercicio 9, y explica qué
hace cada línea usando comentarios de una sola línea.
"""

#Ejercicio 1
print ("Hola mundo")

#Ejercicio 2

#El código del Ejercicio 1 imprime en consola la cadena de texto hola mundo

#Ejercicio 3

print("Mariana", 36)

#Ejercicio 4

print(type("Tipo de dato string",))

print(type(36))

print(type(1.5))

#Ejercicio 5

"""
Los tipos de datos en Python
son las categorias en las que se clasifican los valores
que puedes almacenar y manipular en un programa.
Estos tipos definen que operaciones se pueden realizar sobre los datos y
como se almacenan en la memoria
Tipos de datos básicos: 
- Númericos: int (números enteros),
float (números decimales), 
compex (números complejos)
- Booleanos: True o False
- Texto: cadenas de carácteres
- Secuencias: Estructuras de datos ordenadas
list (listas mutables [])
tuple (tuplas inmutables ())
range (rango de números)
- Conjuntos: colecciones de elementos unicos sin orden especifico
set (conjunto mutable {})
frozenset (conjunto inmutable ({}))
- Mapas: estructuras clave valor
dict (diccionarios {})

Tipos de datos especiales: 
NoneType(representa la ausencia de valor)

Ejemplos:

numero = 10          # int
pi = 3.14           # float
texto = "Python"    # str
es_mayor = True     # bool
lista = [1, 2, 3]   # list
tupla = (4, 5, 6)   # tuple
conjunto = {7, 8, 9} # set
diccionario = {"clave": "valor"} # dict
nulo = None         # NoneType

"""

#Ejercicio 6

print("Hola " + "mundo")

#Ejercicio 7

name = "Mariana"
age = 36

print(name, age)

#Ejercicio 8

name = input("¿Cuál es tu nombre?: ")

print("Hola", name)

#Ejercicio 9

# num1 = 1 creo una variable y guardo un valor
# num2 = 2 creo otra variable y guardo un valor
# sum = num1 + num2 creo una variable que guarde la suma de los valores de las variables creadas

# print(sum, type(sum)) imprimo en pantalla el resultado de la suma y el tipo de dato. 

#Ejercicio 10

#comentar y explicar el ejercicio 9
