"""
1. Realiza las siguientes operaciones aritméticas:
Suma: 15 + 25
Resta: 50 - 22
Multiplicación: 8 * 7
División: 100 / 20
2. Calcula el resto de la división de 37 entre 5 y
almacénalo en una variable remainder. Luego imprímelo.
3. Convierte el número 7 en una cadena de texto y
concaténalo con la frase “ es mi número favorito”.
Imprime el resultado.
4. Repite la palabra “Python” 10 veces usando el operador
de multiplicación para cadenas y luego imprímela.
5. Crea dos variables: a y b con los valores 12 y 8
respectivamente. Compara si a es mayor que b y almacena
el resultado en una variable booleana resultado. Imprime
el valor de resultado.
6. Compara dos cadenas de texto (“apple” y “banana”) usando
los operadores > y < y explica cuál tiene mayor orden
alfabético.
7. Realiza una comparación lógica usando and para verificar
si el número 10 es mayor que 5 y menor que 20. Imprime
el resultado.
8. Usa el operador or para verificar si el número 7 es
menor que 3 o mayor que 5. Imprime el resultado.
9. Aplica el operador not para invertir el resultado de la
comparación 15 > 20. ¿Cuál es el resultado?
10. Combina operadores aritméticos y lógicos: Verifica
si el número resultante de la expresión (5 * 3) + 2 es
mayor que 10 y menor que 20. Imprime el resultado

"""

#Ejercicio 1
print ("-------------")

print(15 + 25)
print(50 - 22)
print(8 * 7)
print(100 / 20)

#Ejercicio 2
print ("-------------")

remainder = 37 % 5
print(remainder)

#Ejercicio 3
print ("-------------")

num = 7
print(type(num))
num= str(num)
print(type(num))

print("El", num, "es mi número favorito")

#Ejercicio 4
print ("-------------")

print("Python " * 10)

#Ejercicio 5
print ("-------------")

a = 12
b = 8

result = a > b

print(result)

#Ejercicio 6 => 
print ("-------------")
# en Python las cadenas de texto (strings) se comparan lexicográficamente, es decir, siguiendo el orden alfabético basado en el valor ASCII de cada carácter.
# La primera letra de "apple" es 'a' y la primera letra de "banana" es 'b'.
# 'a' tiene un valor de 97 y 'b' tiene un valor de 98.
print("apple" > "banana") 
print("apple" < "banana")

#Ejercicio 7
print ("-------------")

print(10 > 5 and 10 < 20)

#Ejercicio 8
print ("-------------")

print (7 < 3 or 7 > 5)

#Ejercicio 9
print ("-------------")

print (not(15 > 20))

#Ejercicio 10
print ("-------------")

print((5*3) + 2 > 10 and (5*3) + 2 < 20)

