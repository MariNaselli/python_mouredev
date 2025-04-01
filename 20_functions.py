"""
Funciones
Son bloques de codigo reutilizables que nos permiten organizar
nuestro codigo de manera eficiente, reducir la repeticion y hacerlo mas legible y facil de mantener

Las funciones nos permiten dividir grandes programas en pequeñas piezas manejables, facilitando
la comprension y el mantenimiento de nuestro codigo

Nos permiten ejecutar una secuencia de instrucciones llamandolas por su nombre

Se cran funciones con la palabra clave def
funciones con parametros
funciones con valores de retorno
parametros con valores por defecto
Funciones con un numero arbitrario de argumentos

Se encapsula el codigo dentro de una funcion y lo llamamos siempre que lo necesitamos
Esto hace un programa mas organizado y facil de entender

Ademas las funciones facilitan la depuracion y el mantenimiento del codigo a largo plazo



"""


def my_function ():
    print("Esto es una función")
    
my_function()

def sum_two_values (first_number, second_number):
    print(first_number + second_number)
    
sum_two_values(8,2)

#la funcion puede recibir parametros como vimos, y tambien lo puede retornar

def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value

sum_two_values_with_return(10, 5)

#tengo que pasar el resultado a una variable

my_result = sum_two_values_with_return(10, 5)
print(my_result)

#lo almaceno en una variable

def sum_values (first, second):
    my_sum = first + second
    return my_sum

def print_name (name, surname):
    print(f"{name} {surname}")

print_name("Mariana", "Naselli")

#aunque no sigamos el orden de llamada podemos definirlo

print_name(surname="Naselli", name="Mariana")

def print_name_with_default (name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")
    
print_name_with_default("Mariana","Naselli", "MariNaselli")
print_name_with_default("Mariana","Naselli")
#puedo agregar un valor por defecto en los parametros si alguien no pone por ejemplo el alias

def print_texts(*text):
    print(text)
    
print_texts("hola", "si", "como")

#al poner un asterisco le paso la cantidad de parametros que quiera
#es un numero de parametros dinamico

def print_texts_(*texts):
    for text in texts:
        print(text)
        
print_texts_("Hola", "Como", "Estas")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
        
print_upper_texts("Hola", "Mari", "Cane", "Panchi")

#no es mandar una lista.



