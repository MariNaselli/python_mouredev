"""
Tuplas
1. Crea una tupla con los valores (10, 20, 30, 40, 50) e
imprímela.
2. Accede al segundo elemento de la tupla (100, 200, 300,
400, 500) y muéstralo.
3. Intenta modificar el primer elemento de la tupla (1, 2,
3) a 10 y observa el resultado.
4. Cuenta cuántas veces aparece el número 3 en la tupla (1,
2, 3, 3, 4, 5, 3).
5. Encuentra el índice de la primera aparición de la cadena
"Python" en la tupla ("Java", "Python", "JavaScript",
"Python").
6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la
tupla resultante.
7. Crea una subtupla con los elementos desde la posición 2
hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30,
40, 50).
8. Convierte la tupla ("rojo", "verde", "azul") en una
lista, cambia el segundo elemento a "amarillo" y vuelve
a convertirla en una tupla. Imprime la tupla resultante.
9. Elimina una tupla llamada my_tuple usando del y luego
intenta imprimirla para ver el resultado.
10. Crea una tupla con un solo elemento (el número 100)
e imprímela. Asegúrate de usar la sintaxis correcta para
crear una tupla con un solo elemento.
"""

#Ejercicio 1

my_tuple = (10, 20, 30, 40, 50)

print(my_tuple)
print(type(my_tuple))

#Ejercicio 2
print("-------------")

other_tuple = (100, 200, 300, 400, 500)
print(other_tuple[2])

#Ejercicio 3
print("-------------")

#other_tuple[0] = 50
#no se puede modificar el elemnto de una tupla 

#Ejercicio 4
print("-------------")

count_tuple = (1,2, 3, 3, 4, 5, 3)

print(count_tuple.count(3))

#Ejercicio 5
print("-------------")

string_tuple = ("Java", "Python", "JavaScript","Python" )

print(string_tuple.index("Python"))

#Ejercicio 6
print("-------------")

tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)

concatenar_tuplas = tuple_1 + tuple_2

print(concatenar_tuplas)

#Ejercicio 7
print("-------------")

sub_tuple = my_tuple[2:4]

print(sub_tuple)

#Ejercicio 8
print("-------------")

una_tupla = ("rojo", "verde", "azul")

una_tupla = list(una_tupla)

print(type(una_tupla))

print(una_tupla)

una_tupla[2] = "Amarillo"
print(una_tupla)

una_tupla = tuple(una_tupla)

print(type(una_tupla))

#Ejercicio 9
print("-------------")

my_my_tuple = ( 3, 6, 8, 4)

del my_my_tuple

#print (my_my_tuple) # => no esta definida da error. 

#Ejercicio 10
print("-------------")

tuple = (100, ) # => usar la coma para que no lo tome como entero

print(tuple)

print(type(tuple))

