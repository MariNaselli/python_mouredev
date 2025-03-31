"""
Bucles
1. Usa un bucle while para imprimir los números del 1 al
10.
2. Usa un bucle for para recorrer la lista[10, 20, 30, 40,
50] e imprime cada número.
3. Escribe un programa que use un bucle while para sumar
los números del 1 al 100 e imprime el resultado.
4. Escribe un bucle for que imprima cada carácter de la
cadena “Python”.
5. Usa un bucle while para encontrar el primer número
divisible por 7 entre 1 y 50.
6. Usa un bucle for para recorrer el diccionario {“name”:
“Brais”, “age”: 37, “country”: “Galicia”} e imprime las
claves.
7. Escribe un programa que use un bucle while para imprimir
los números pares entre 1 y 20.
8. Usa un bucle for con la función range() para imprimir
los números del 1 al 10 en orden inverso.
9. Escribe un programa que use un bucle for para contar
cuántas veces aparece el número 30 en la lista[30, 10,
30, 20, 30, 40].
10. Usa un bucle for para recorrer una lista de nombres
y detener el bucle cuando se encuentre el nombre
“Brais”.
"""

#Ejercicio 1

my_condition = 0

while my_condition <10:
    my_condition +=1
    print(my_condition)
    
#Ejercicio 2

print("------------------")

my_list =  [10, 20, 30, 40, 50]

for numbers in my_list:
    print(numbers)

#Ejercicio 3
    
print("------------------")

contador = 1
suma_total = 0

while contador <= 100:
    suma_total += contador
    contador += 1

print("La suma del 1 al 100 es:", suma_total)

#Ejercicio 4

print("------------------")

for letra in "Python":
    print(letra)

#Ejercicio 5
print("------------------")

num = 1

while num <=50:
    if num % 7 == 00:
        print("El primer número divisible por 7 es: ", num)
        break
    num += 1
    
#Ejercicio 6
print("------------------")

my_dict = {"name": "Brais", "age": 37, "country": "Galicia"}

for element in my_dict:
    print(element)
    
#Ejercicio 7
print("------------------")
num_ = 1

while num_ <= 20:
    if num_ % 2 == 0:
        print(num_)
    num_ += 1
    
#Ejercicio 8
print("------------------")

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in range(len(list_num)-1, -1, -1):
    print(num)
    
#Ejercicio 9
print("------------------")

una_lista = [30, 10,30, 20, 30, 40]

contador_ = 0

for num in una_lista:
    if num == 30:
        contador_ += 1
        
print (f"El numero 30 aparece {contador_} veces en la lista")


#Ejercicio 10
print("------------------")

lista_nombres = ["Mariana", "Meli", "Canela", "Brais", "Panchi", "Menta"]

for nombre in lista_nombres:
    print(nombre)
    if nombre == "Brais":
        break
    
