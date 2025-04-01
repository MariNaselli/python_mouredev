"""
Excepciones
Errores
Tenemos que tener mecanismos de manejo de errores

try
    run code
except
    except
else
    pase lo que pase
finally
"""

number_one = 5
number_two = 3

number_two = "3"

#print(number_one + number_two)

try: 
    print(number_one + number_two)
except:
    print("Se ha producido un error")

num_one= 1
num_two= 2
try:
    print(num_one + num_two)
except:#se ejecuta si se produce una excepcion
    print("Se ha producido un error")
else: #esto se ejecuta si NO se produce una excepcion => es opcional
    print("La ejecución continúa correctamente")
finally:#se ejecuta siempre pase lo que pase => es opcional
    print("La ejecución continúa")
    
#la captura de excepciones por tipo

num_1 = 3
num_2 = "4"

try:
    print(num_1 + num_2)
except TypeError: #se ejecuta solo si se produce TypeError
    print("Se ha producido un error de TypeError")
except ValueError:
    print("Se ha producido un ValueError")
    
#segun si queremos capturar errores muy concretos

#captura de la informacion de la excepcion = >

try:
    print(num_1 + num_2)
except ValueError as error: #una variable que captura la informacion de la excepcion
    print(error) #esto no se cumple se captura la excepcion generica debajo
except Exception as error: #forma de controlar el error
    print(error)


    

    
