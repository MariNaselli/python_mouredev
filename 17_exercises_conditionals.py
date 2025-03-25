"""
Condicionales
1. Escribe un programa que verifique si un número es
positivo, negativo o cero.
2. Solicita al usuario que ingrese su edad y muestra un
mensaje indicando si es mayor de edad(18 años o más) o
menor de edad.
3. Escribe un programa que verifique si una cadena de texto
está vacía y muestre un mensaje en consecuencia.
4. Crea un programa que solicite dos números al usuario y
compare cuál es mayor. Si son iguales, muestra un
mensaje indicando la igualdad.
5. Escribe un programa que verifique si un número es
divisible por 3 y por 5 al mismo tiempo.
6. Solicita al usuario que ingrese un número y verifica si
es par o impar.
7. Escribe un programa que determine si una persona puede
votar en función de su edad(mayor o igual a 18). Si
tiene 16 o 17 años, indica que puede votar con permiso
especial.
8. Crea un programa que solicite una contraseña al usuario
y verifique si coincide con una contraseña predefinida.
Si no coincide, muestra un mensaje de error.
9. Escribe un programa que determine si un número está
entre 10 y 20 (ambos incluidos).
10. Escribe un programa que simule un semáforo:
solicita al usuario que ingrese un color(rojo, amarillo,
verde) y muestra un mensaje indicando si debe detenerse,
estar alerta o avanzar.
"""

# Ejercicio 1
my_number = 0

if my_number > 0:
    print("Este número es positivo")
elif my_number < 0:
    print("Este número es negativo")
else:
    print("Este número es 0")
    
print("-------------------")

#Ejercicio 2

my_age = int(input("Cual es tu edad?"))

if my_age >= 18:
    print("Es mayor de edad")
else: 
    print("Es menor de edad")
    
"""
try:
    my_age = int(input("Cual es tu edad?: "))

    if my_age >= 18:
        print("Es mayor de edad")
    else: 
        print("Es menor de edad")
    
except ValueError:
    print("Por favor ingresa un número válido")
"""

print("-------------------")

#Ejercicio 3

my_string = ""

if not my_string:
    print("La cadena de texto está vacía")

print("-------------------")

#Ejercicio 4

first_number = int(input("Ingresa un número: "))

second_number = int(input("Ingresa otro número: "))

if first_number == second_number:
    print("Los números ingresados son igules")

else:
    print("Los números ingresados no son iguales")
    
#Ejercicio 5

print("-------------------")

number = int(input("Ingresa un número: "))

if number % 3 == 0 and number % 5 == 0:
    print("El número es divisible por 3 y por 5")
    
else:
    print("El número no es divisible por 3 y por 5")
    
#Ejercicio 6

print("-------------------")

other_number = int(input("Ingresa un número: "))

if other_number % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
    
#Ejercicio 7

print("-------------------")

age_votar = int(input("Ingrese su edad: "))

if age_votar >=16 and age_votar <= 17:
    print("Con permiso especial podés votar") 
elif age_votar >= 18:
    print("Podés votar")
else:
    print("No tenés edad para votar")
    

#Ejercicio 8

print("-------------------")

insert_password = int(input("Ingrese la contraseña: "))

password = 12345

if insert_password == password:
    print("Tu contraseña es válida")
else:
    print("La contraseña no es válida")
    

 #Ejercicio 9

print("-------------------")   

entry_number = 4

if entry_number >= 10 and entry_number <= 20:
    print("El número está entre 10 y 20")
else:
    print("El número es menor que 10 o mayor que 20")
    
#Ejercicio 10

print("-------------------") 
    
color_semaforo = input("Ingrese un color entre rojo, amarillo o verde: ")

if color_semaforo == "rojo":
    print("Detenerse!")
elif color_semaforo == "verde":
    print ("Avance!")
elif color_semaforo == "amarillo":
    print ("Alerta!")
else:
    print ("Ingrese un color rojo, verde o amarillo")
