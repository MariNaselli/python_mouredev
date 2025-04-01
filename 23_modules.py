"""
Modulos

codigo externo a nuestro proyecto y queremos utulizarlo, entra el concepto de modulos
(relacionado a librerias)

al tener muchos ficheros, si quiero que mi programa sea escalable y seguro
tengo que usar esos ficheros desde otro

es esa libreria, ese lugar donde tenemos codigo. 
esto es para no replicar codigo, sino usar los modulos

"""
import module
# from module import sum => puedo llamarlo concretamente
# y no hace falta que lo llame con module.sum

#sum()

module.sum(4, 5, 6)

module.print_value("Hola Mari")

from module import sum

sum(2, 5, 6)

#python tiene diferentes modulos que podemos utilizar
