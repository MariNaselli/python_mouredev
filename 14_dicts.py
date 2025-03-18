"""
Los diccionarios son colecciones que almacenan pares clave-valor
permitiendo acceder a los valores de manera rapida mediante su clave.
Esto los hace perfectos para representar datos estructurados, como las entradas
de una base de datos o la configuracion de una aplicacion.

Un diccionario se puede definir usando llaves o la funcion dict()
Los elementos dentro del diccionario se organizan como pares de clave y valor, separados por dos puntos :

A los elementos en un diccionario se acceden mediante su clave en lugar de su indice numerico
Si se intenta acceder a una clave que no existe se lanza un error

Los diccionarios son mutables lo que se puede modificar, agregar, o eliminar elementos despues de su creacion.
Se puede agregar un nuevo par clave-valor simplemente asignandolo o avtualizar el valor de una clave existente

Se puede eliminar un par clave valor usando la instruccion del

Operaciones comunes:
Tienen varios metodos utiles como keys() para obtener todas las claves
values() para obtener todos los valores
items() para obtener pares clave-valor

Comprobacion de claves: Podemos comprobar si una clave esta presente en un diccionario utilizando el operador in
esto es util para verificar su existencia antes de acceder a ella

Los valores de un diccionario pueden ser de cualquier tipo de datos incluyendo otros diccionarios
Esto permite la creacion de diccionarios anidados. es util para representar estructuras de datos mas complejas

Conversion de Listas a diccionarios; Python lo permite utilizando fromkeys(), que crea un diccionario donde las claves provienen de la lista y los valores pueden
ser definidos o dejados vacios
"""

my_dict = dict()
print(type(my_dict))

my_other_dict = {}
print(type(my_other_dict))

my_other_dict = {"Nombre":"Mariana", "Apellido":"Naselli", "Edad":35}
print(my_other_dict)

my_dict = {
    "Nombre":"Mariana", 
    "Apellido":"Naselli", 
    "Edad":35,
    "Leguajes": {
        "Python",
        "Java",
        "PHP"
    }
    }

print(my_dict)

print(my_dict["Nombre"])

my_dict["Nombre"] = "Graciela"
print(my_dict["Nombre"])

my_dict["Direccion"] = "Ancora 16"
print(my_dict)

del my_dict["Direccion"]
print(my_dict)

print("Graciela" in my_dict) # => da false porque no busca por valor
print("Nombre" in my_dict)

print(my_dict.items()) # => Listado clave valor
print(my_dict.keys()) # => listado de las claves
print(my_dict.values()) # => listado de los valores

my_new_dict = my_other_dict.fromkeys(("Nombre", "Apellido"))
print(my_new_dict)

print(my_other_dict)

# dict.fromkeys(claves, valor_por_defecto)

#Creamos un diccionario con las claves y todas tienen none como valor

claves = ["nombre", "edad", "ciudad"]

diccionario = dict.fromkeys(claves)

print(diccionario)

#Creamos diccionaro con valor por defecto

claves = ["nombre", "edad", "ciudad"]

diccionario = dict.fromkeys(claves, "Desconocido")

print(diccionario)

#Creamos diccionarios con valores iniciales en 0

productos = ["manzana", "naranja", "pera"]

inventario = dict.fromkeys(productos, 0)

print(inventario)

#Copiar claves de otros diccionarios con valores vacios

datos_originales = {"nombre":"Mariana", "apellido":"Naselli", "edad":35, "ciudad":"Madrid"}

diccionario_nuevo = dict.fromkeys(datos_originales.keys())

print(diccionario_nuevo)