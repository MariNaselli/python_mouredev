"""
Diccionarios
1. Crea un diccionario con las claves name, age, y country,
asignando valores a cada una. Imprime el diccionario.
2. Accede al valor de la clave name en el diccionario.
3. Añade una nueva clave job con el valor "Programador" al
diccionario del punto anterior. Imprime el diccionario
actualizado.
4. Modifica el valor de la clave age en el diccionario para
que sea 38. Imprime el diccionario actualizado.
5. Elimina la clave country del diccionario e imprime el
diccionario resultante.
6. Crea un diccionario donde las claves sean números del 1
al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2:
4, ...).
7. Verifica si la clave age está presente en el diccionario
{"name": "Brais", "age": 37, "country": "Galicia"}.
8. Imprime solo las claves del diccionario.
9. Convierte las claves del diccionario en una lista e
imprime la lista resultante.
10. Crea un nuevo diccionario a partir de una lista de
claves ["name", "age", "job"] usando fromkeys(),
asignando a todas las claves el valor "Desconocido".
"""
#Ejercicio 1
my_dict = {"name":"Mariana", "age":36, "country": "España"}

print(my_dict)
print(type(my_dict))

#Ejercicio 2

print(my_dict["name"])

#Ejercicio 3

my_dict["job"] = "Programador"

print(my_dict)

#Ejercicio 34

my_dict["age"] = 38
print(my_dict)

#Ejercicio 5

del my_dict["country"]

print(my_dict)

#Ejercicio 6

diccionario_cuadrados = {1:1, 2:4, 3:9, 4:16, 5:25 }

print(diccionario_cuadrados)

#Ejercicio 7

print("age" in my_dict)

#Ejercicio 8

print(my_dict.keys())

#Ejercicio 9

my_list = list(my_dict)

print(my_list)

#Ejercicio 10

my_new_dict = dict.fromkeys(my_list, "Desconocido")

print(my_new_dict)

