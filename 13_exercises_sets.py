"""
1. Crea un set con los números del 1 al 5 e imprímelo.
2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.
3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5}
nuevamente. ¿Qué sucede?
4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e
imprime el resultado.
5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el
set resultante.
6. Usa el método clear() para vaciar un set y luego imprime
su longitud.
7. Convierte el set {"manzana", "naranja", "plátano"} en
una lista e imprime el primer elemento de la lista.
8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e
imprime el set resultante.
9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3,
4, 5, 6} e imprime el resultado.
10. Elimina un set llamado my_set usando del y luego
intenta imprimirlo para ver el resultado.
"""
#Ejercicio 1

my_set = {1, 2, 3, 4, 5}

print(my_set)

print(type(my_set))

#Ejercicio 2
print("---------------")

my_set.add(6)

print(my_set)

#Ejercicio 3
print("---------------")

my_set.add(5)

print(my_set)

#no da error, pero no lo agrega porque ya existe

#Ejercicio 4
print("---------------")

print(3 in my_set )

#Ejercicio 5
print("---------------")

my_set.remove(4)

print(my_set)

#Ejercicio 6
print("---------------")

un_set = {4, 5, 6}

print(un_set)

un_set.clear()

print(len(un_set))

#Ejercicio 7
print("---------------")

otro_set = {"Manzana", "Naranja", "Pera"}

convertir_set = list(otro_set)

print(type(convertir_set))

print(convertir_set)

print(convertir_set[0])

#el tipo de dato cambia pero el orden de los elementos no estan garantizados
#cuando lo convierto en list los elementos siguen sin un orden predecible porque el ser los almaceno de forma desordenada

#puedo ordenarla y establecer un orden garantizado asi:

convertir_set = sorted(otro_set)
print(convertir_set)
print(convertir_set[0])

#Ejercicio 8
print("---------------")

set1 = {1, 2, 3 }
set2 = {4, 5, 6}

union_set = set1.union(set2)

print(union_set)

#Ejercicio 9
print("---------------")

print(set1.difference(set2))
print(set2.difference(set1))

#Ejercicio 10
print("---------------")

eliminar_set = {"Hola", "Mari"}

del eliminar_set

# print(eliminar_set) NameError: name 'eliminar_set' is not defined