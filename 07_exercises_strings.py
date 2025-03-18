"""
Cadenas de texto
1. Declara una variable text con la frase “Aprendiendo
Python” y luego imprime la longitud de la cadena usando
len().
2. Concatena dos cadenas: “Hola” y “Python”, y muestra el
resultado en una sola línea.
3. Crea una cadena que incluya un salto de línea, y luego
imprímela para ver el resultado.
4. Usa el formateo de cadenas con f-strings para imprimir
tu nombre, apellido y edad en una cadena de texto.
5. Desempaqueta los caracteres de la palabra “Python” en
variables separadas y luego imprímelos uno por uno.
6. Extrae un “slice” de la palabra “Programación” para
obtener los caracteres desde la posición 3 hasta la 7.
7. Invierte la cadena “Python” usando slicing y muestra el
resultado.
8. Convierte la cadena “aprendiendo python” en mayúsculas
usando el método adecuado e imprímela.
9. Cuenta cuántas veces aparece la letra “n” en la cadena
“Programación en Python”.
10. Verifica si la cadena “12345” es numérica usando el
método adecuado e imprime el resultado.
"""

#Ejercicio 1

text = "Aprendiendo Python"

print(len(text))

#Ejercicio 2

print("----------------------")
print("Hola" + " " + "Python")

#Ejercicio 3
print("----------------------")
print("Cadena con\nsalto de línea")

#Ejercicio 4
print("----------------------")

name, surname, age = "Mariana", "Naselli", 36

print(f"Mi nombre es {name} {surname} y tengo {age} años")

#Ejercicio 5

a, b, c, d, e, f = "Python"

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Ejercicio 6

print("-------------------")

palabra = "Programación"

slice_programacion = palabra [3:7]

print(slice_programacion)

#Ejercicio 7

#Ejercicio 6

print("-------------------")

cadena_python = "Python"

reversed_cadena_python = cadena_python[::-1]

print(reversed_cadena_python)

#Ejercicio 8
print("-------------------")
print(text.upper())

#Ejercicio 9
print("-------------------")

new_text = "Programación en Python"

print(new_text.count("n"))

#Ejercicio 10
print("-------------------")

cadena = "12345"

print(cadena.isnumeric())