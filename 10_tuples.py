"""
Es una estructura de datos similar a las listas
con la diferencia clave de que son inmutables
una vez creadas, no pueden modificarse

esto lo hace ideales para almacenar datos que no deben cambiar a lo largo de la ejecucion
del programa, aportando mas seguridad

Las tuplas se pueden crear utilziando () o la operacio tuple()
al igual que las listas pueden almacenar multiples tipos de datos

Accedemos a los elementos utilizando indices

Se puede usar el count() para saber cuantas veces aparece un valor y tambien obtener la posicion del primer valor encontrado usando index()

Las tuplas son inmutables pero si se necesitan realizar cambios primero hay que convertirla en una lista
modificarla y luego convertirla en tupla nuevamente

se pueden concatenar tuplas, tambien se pueden extraer una subtupla

Eliminacion: no es posible eliminar elementos individuales de una tupla, se puede eliminar la tupla completa usando la instruccion del


"""

my_tuple = tuple()

my_other_tuple = ()

my_tuple = (35, 1.77, "Mari", "Naselli")

my_other_tuple = (35, 60, 30, 20)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Mari"))

print(my_tuple.index(35))

print(my_tuple + my_other_tuple) # => se pueden concatenar

#=> si quiero una tupla mutable en realidad quiero una lista
my_tuple = list(my_tuple)
print(type(my_tuple))

print(my_tuple)
my_tuple.append("MariNase")

print(my_tuple)

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple

print(my_tuple) # => NameError: name 'my_tuple' is not defined


