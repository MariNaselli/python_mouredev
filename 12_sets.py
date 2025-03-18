"""
Son estructuras de datos ideales para almacenar elementos unicos y realizar
operaciones como la union, interseccion y diferencia.
Los sets en Python son colecciones no ordenadas y sin elementos duplicados, los que los hace muy
eficientes cuando se trata de realizar busquedas y operaciones entre conjuntos de datos

Un set se define utilizando la funcion set() o llaves {}
Es importante saber que si se usa llaves vacias esto creara un diccionario vacio, por lo que se debera
usar un set() para inicializar un set vacio. 

Incercion de elementos: Se pueden agregar elementos con el metodo add() pero recordar que los set no permiten
elementos duplicados. Si se intenta agregar un valor que ya existe no producira ningun cambio

Busqueda de elemento: Verificaremos si un valor especifico esta presente en un set utilizando el valor in. Este tipo de busqueda es muy eficiente
en los sets, dado que estan optimizados para esas operaciones

Eliminacion de elementos: Podemos eliminar elementos de un set utilizando el metodo remove()
que produce un error si el elemento no existe, o discard() que no genera error en caso que el elemento no este presente
tambien podemos vaciar un set con con clear()

Transformacion entre sets y listas: los sets no estan ordenanos, pero podemos convertirlos en listas para acceder a elementos mediantes indices. Esta conversion es utli
cuando necesitamos acceder a un elemento especifico

Operaciones con sets: Permiten utulizar varias operaciones de teoria de conjuntos, como la union() que combina los elementos de dos sets y la diferencia difference() que devuelve los elementos que estan en un set
pero no en otro. 
"""

#Digamos que de base tiene atras una lista...

my_set = set()
my_other_set = {}

print(type(my_set)) #=> es un tipo de dato
print(type(my_other_set)) # => me dice que es un diccionario

my_other_set = {"Mariana", "Naselli", 36}
print(type(my_other_set)) # => ahora me dice que es un diccionario

#si lo definimos el set vacio nos dice que es un diccionario.. 
#en el momento que le metemos datos si es un set

print(len(my_other_set)) # => 3 elementos

#print(my_other_set[0]) asi no puedo acceder a un elemento como en una lista

my_other_set.add("MariNaselli") # => un set no es una estructura ordenada, me agrego esto al principio
print(my_other_set) 

#por eso no puedo acceder al elemento 1, 0, etc.. #porque nunca se donde está, si quiero acceder no puedo, es un orden aleatorio

my_other_set.add("MariNaselli") # => si lo vuelvo a agregar no lo hace, y ahora me lo muestra al ultimo

#un set no admite repetidos, otra diferencia con tuplas y listas

print("Mariana" in my_other_set) # => true
print("Mara" in my_other_set) # => False

#podemos consultar

my_other_set.remove("Mariana")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) # => me da error

#no confundir clear que del.. 

my_set = {"Mari", "Naselli", 36}
my_list = list(my_set)

print(my_list)

print(type(my_list))

print(my_list)

print(my_list[0])

#esto no es recomendable 

my_other_set = {"Python", "Angular", "MySql"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"JavaScript"}))

print(my_new_set.difference(my_set))