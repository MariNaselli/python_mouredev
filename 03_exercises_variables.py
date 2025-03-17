"""
1. Declara y asigna valores a las siguientes variables:
name: una cadena que contenga tu nombre.
age: un número entero que represente tu edad.
height: un número flotante que represente tu altura.
Imprime cada variable en una línea separada.
2. Convierte la variable edad de entero a cadena y
concatenala con un texto que diga cuántos años tienes.
3. Declara una variable booleana is_student que indique si
eres estudiante o no. Usa True o False según corresponda
e imprímela.
4. Usa la función len() para calcular cuántos caracteres
tiene tu nombre completo, almacenado en una variable.
5. Declara tres variables en una sola línea que representen
tu nombre, apellido y ciudad de origen. Luego, imprime
estos valores.
6. Usa la función input() para solicitar al usuario su
color favorito y almacénalo en una variable color.
Luego, imprime el valor ingresado.
7. Declara una variable fruit e inicialízala con un valor.
Luego, cambia el valor de la fruta a otro diferente y
vuelve a imprimirla.
8. Convierte un número decimal, almacenado en la variable
price, a un número entero y luego imprímelo.
9. Declara una variable llamada address_len y almacena en
ella la cantidad de caracteres de una dirección usando
la función len(). Imprime el resultado.
10. Usa un tipo de dato forzado para declarar una
variable phone, asegurándote de que siempre será un
número. Luego, cambia su valor a un número di
"""

# Ejercicio 1

name = "Mariana"
age = 36
height = 1.58

print(name)
print(age)
print(height)

#Ejercicio 2

age = str(age)
print(type(age))

print("Tengo", age, "años")

#Ejercicio 3

is_student = True

print(is_student)

#Ejercicio 4

print(len(name))

#Ejercicio 5

name, lastname, city = "Mariana", "Naselli", "Córdoba"

print("Mi nombre es", name, lastname, "y mi ciudad de origen es", city)

#Ejercicio 6

# color = input("¿Cuál es tu color favorito?: ")

# print("Mi color favorito también es", color,"!")

#Ejercicio 7

fruit = "Manzana"

print(fruit)

fruit = "Naranja"

print(fruit)

#Ejercicio 8

price = 1.30

print(type(price))

price = int(price)

print(int(price))

#Ejercicio 9

address = "Carrer Ancora 16"
address_len = len(address)

print(address_len)

#Ejercicio 10

phone: int = 663999999

print(type(phone))

phone = 11111111

print(type(phone))



