# Variables => convenciones minuscula y snake_case

my_string_variable = "My String"

print(my_string_variable) 

my_int_variable = 5

print (my_int_variable)

my_bool_variable = True

print(my_bool_variable)

#Concatenación de variables

print(my_string_variable, my_int_variable)


my_int_to_str_variable = str(my_int_variable) #transformamos el entero en una cadena de texto

print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

#Funciones del sistema

print(len(my_string_variable)) #Cuenta los caracteres

#Los print concatenando => ej. cadena de texto + bool.

print("Este es el valor de:", my_bool_variable)

#Variables en una sola línea => no recomendable...

name, surname, alias, age = "Mariana", "Naselli", "MariNaselli", 36

print("Mi nombre es:", name, surname,".Mi alias es:" , alias,".Y mi edad es:",  age)

#inputs

# first_name = input("What is your name?: ")
# age = input("How old are you?: ")

# print(first_name)
# print(age)

# print(name)

#Python no tiene tipado fuerte, se puede cambiar el tipo de dato

name = 36
age = "Mariana"

print (name, age)

#Identificamos el tipo

address: str = "Mi dirección"
print(address)
address = 32
print (type(address))
