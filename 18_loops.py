"""
Loops => bucles /ciclos

Los bucles nos permiten repetir bloques de codigo de forma eficiente, evitando la necesidad de escribir el mismo codigo una y otra vez. 
En p. los bucles son esenciales para trabajar con colecciones de datos y
ejecutar tareas repetitivas de manera rapida y limpia. 
Los dos tipos principales de bucles son el while y el for

El bucle while ejecuta un bloque de codigo mientras una condicion
sea verdadera. Es ideal cuando no sabemos exactamente cuantas veces se debe repetir el ciclo,
pero tenemos una condicion que debe cumplirme para continuar la ejecucion. 

El bucle for se utiliza para iterar sobre colecciones de datos, como listas, tuplas, sets, diccionarios. 
Es perfecto para recorrer una coleccion de forma ordenada


"""

# pasar por el mismo codigo varias veces

#while => mientras sea verdadero haz algo

#my_condition = 0
#while my_condition < 10:
#print(my_condition)
#eso es un bucle infinito => porque la condicion nunca cambia


my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition +=2
else:
    print("Mi condición es mayor o igual que 10")
#hasta que my condition se pase de 10
#cuando no cumple la condicion, le podemos meter un else.
#tendriamos un control exacto de cuando no se cumple 

#esto seria como una especie de if que se repite..

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene mi condición")
        break
    print(my_condition)
    
#un for es cumplir una condicion. Para iterar un listado de elementos
print("---Lista---")
my_list = [35, 24, 62, 52, 30, 30, 17]
#guardan elementos de forma ordenada, de uno en uno.
for numbers in my_list:
    print(numbers)
#un bucle mas atado a un numero de elementos digamos, en este caso de numeros. 
print("---Tupla---")
my_tuple = (35, 1.77, "Mari", "Naselli", "MariNaselli")
#guardan elementos pero no se pueden retocar

for element in my_tuple:
    print(element)
print("---Set---")
my_set = {"Mari", "Naselli", 35}
#guardan elementos que no estan repetidos

for element in my_set:
    print(element)
    
print("---Diccionario---")
my_dict = {"Nombre":"Mariana", "Apellido":"Naselli", "Edad": 36}
#guardan elementos de forma clave valor    

for element in my_dict:
    print(element)
    if element == "Apellido":
        break


