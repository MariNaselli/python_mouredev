"""
if, elif y else para controlar el flujo de ejecucion dependiendo si
una condicion se cumple o no

Una condicional evalua si una expresion es verdadera o falsa
Si es verdadera el codigo dentro del bloque if se ejectuta
Si no es verdadera podemos usar otras opciones como elif que es else if para evaluar
mas condiciones o else para manejar el caso en que ninguna de las condiciones anteriores se cumpla.

El condicional if es una estructura que permite que un bloque de codigo se ejecute solo si una condicion especifica se cumple

El condicional elif nos permite evaluar condiciones adicionales cuando la primera condicion no se ha cumplido

El condicional else es el bloque final que se ejecuta cuando ninguna de las condiciones anteriores es verdadera
"""

my_condition = False

if my_condition: #esta implicito el true
    print("Se ejectuta la condición del if")
    
my_condition = 1
if my_condition == 11:
    print("Se ejecuta la condición del segundo if")
    
print("la condición continua")

if my_condition == 10:
    print("Se ejecuta")

if my_condition > 10 and my_condition < 20 :
    print("Es mayor que 10 y menor que 20")
elif my_condition ==1:
    print("Es igual a 1")
    
else:
    print("Es menor o igual que 10 o mayor que 20")

#Si no se cumple nada nuestro programa se va al else
#elif necesita una condicion => otra comprobación
#Hay ordenes de jerarquias.. 
    
    
my_string = "Mi cadena de texto"

if my_string:
    print("Mi cadena de texto NO está vacia")


    