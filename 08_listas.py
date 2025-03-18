"""
Las listas son colecciones ordenandas de elementos 
que pueden almacenar diferentes tipos de datos
y permiten realizar gran variedad de operaciones,
desde la manipulacion de sus elementos 
hasta la creación de sublistas.

usamos list() o []

Una lista puede contener elementos de cualquier tipo de datos e incluso otras listas

Podemos acceder mediante indices, el primer elemento tiene el indice 0
Podmeos acceder a los elementos desde el final de la lista usando indices negativos

Podemos realizar operaciones como concatenacion, repeticion, y busqueda de elementos
Tambien podemos contar cuantas veces aparece un elemento especifico con el metodo count()

Las listas son mutables, lo que significa que podemos modificar sus elementos
Agregar con append() e insert(), eliminar con remove() y pop() y como actualizar valores. 

Podemos copiar y limpiar listas con copy() y clear()

Sublistas y slicing: Podemos crar sublistas a partir de listas utilizando el concepto slicing, que nos permite
extraer porciones de una lista mediante el uso de indices

Ordenacion e inversion: podemos ordenar una lista numerica o alfabetica con sort() e invertir una lista con reverse()


"""

my_list = list()

my_other_list = []

print(len(my_list))

my_list = [35, 24, 55, 67, 45]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.75, "Mari", "Naselli"]

print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])

print(my_other_list[-1]) #elultimo elemento
print(my_other_list[-2])

print(my_list.count(24))

age, height, name, surname = my_other_list

print(name)

print(my_list + my_other_list)

#tener en cuenta esto:

#my_list = "Hola" => va a cambiar y deja de ser una lista y el tipo de dato pasa a ser str.

my_other_list.append("MariNaselli") # => incerta elemento al final
print(my_other_list)

my_other_list.insert(1, "Azul") # => declaro la posicion antes y luego el elemento a incertar
print(my_other_list)

my_other_list.insert(0, "Verde")

my_other_list[0] = "Rojo" # => Modifico el valor de un elemento de la lista

my_other_list.remove("Azul")
print(my_other_list)

print("-------------")
print(my_list)
my_list.pop() # => elimina el ultimo elemento o le puedo pasar el indice del elemento que quiero eliminar
print(my_list)

print(my_list.pop())

my_list.pop(0)

print(my_list)

del my_list[0]
print(my_list)

my_new_list = my_list.copy() #=> copio la lista

my_list.clear()
print(my_list)
print(my_new_list)

#remove => elimina un elemento en concreto
# del => elimina por indice

my_new_list.append(35)

print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.append(12)
print(my_new_list)

my_new_list.sort() # => ordena
print(my_new_list)

print(my_new_list[1:2])
