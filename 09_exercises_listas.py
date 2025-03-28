"""
Listas
1. Crea una lista con los números del 1 al 5 e imprímela.
2. Accede e imprime el tercer elemento de la lista [10, 20,
30, 40, 50].
3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5]
e imprímela.
4. Inserta el número 15 en la posición 2 de la lista [10,
20, 30, 40, 50].
5. Elimina el primer valor 30 de la lista [10, 20, 30, 30,
40, 50].
6. Usa la función pop() para eliminar el último elemento de
la lista [1, 2, 3, 4, 5] y almacénalo en una variable.
Imprime la variable y la lista.
7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.
8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e
imprímela.
9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el
resultado en una nueva lista. Imprime la lista
resultante.
10. Crea una sublista con los elementos de la lista
[10, 20, 30, 40, 50] que van desde la posición 1 hasta
la 3 (sin incluir la posición 3)
"""

#Ejercicio 1

list_num = [1, 2, 3, 4, 5]

print(list_num)
print(type(list_num))

#Ejercicio 2
print("----------------")
new_list = [10, 20, 30, 40, 50]

print(new_list[3])

#Ejercicio 3
print("----------------")

list_num.append(6)
print(list_num)

#Ejercicio 4
print("----------------")

new_list.insert(2, 15)
print(new_list)

#Ejercicio 5
print("----------------")

other_list = [10, 30, 20, 30, 40, 50]

other_list.remove(30)
print(other_list)

#Ejercicio 6
print("----------------")

new_list_num = list_num.pop()
print(new_list_num)
print(list_num)
print(new_list_num)

#Ejercicio 7
print("----------------")

invierte_lista = [100, 200, 300, 400, 500]

invierte_lista.reverse()

print(invierte_lista)

#Ejercicio 8
print("----------------")

ordena_lista = [3, 1, 4, 2, 5]

ordena_lista.sort()

print(ordena_lista)

#Ejercicio 9
print("----------------")

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

lista_concatenada = lista_1 + lista_2

print(lista_concatenada)

#Ejercicio 10
print("----------------")

lista_ = [10, 20, 30, 40, 50]

sublista = lista_[1:3]

print(sublista)