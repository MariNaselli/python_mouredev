"""
clases: objetos
todo lo que este en la clase responde a una cierta logica
si tenemos la clase persona, tendra que tener logica relacionada con persona
ejemplo una funcion dormir, no una funcion volar. 

"""

class EmptyPerson:
    pass
#pass para que ignore/no de error
#los nombres de las clases en mayuscula y camelCase

#print(EmptyPerson)
#print(EmptyPerson())

class Person:
    def __init__(self, name, surname): #constructor de clase => def init self
        self.name = name
        self.surname = surname
    
    def walk(self):
        print(f"{self.name} está caminando")
    
my_person = Person("Mariana", "Naselli")
print(f"{my_person.name} {my_person.surname}")
print(my_person.walk())
my_person.name = "Panchi"
print(f"{my_person.name} {my_person.surname}")

class MyPerson:
    def __init__(self, name, surname, alias = "Sin Alias"):
        self.full_name = f"{name} {surname} {alias}" #Propiedad pública
        self.__name = name #Propiedad privada
        
    def get_name(self):
        return self.__name
        
my_person_ = MyPerson("Brais", "Moure")
print(my_person_.full_name)
print(my_person_.get_name())
#my_person_.full_name = 666
#print(my_person_.full_name)

#objeto que nos sirve para definir una entidad, que en este caso es una persona

#el objeto es mutable es decir en cualquier momento puedo cambiar el tipo de dato
#no es un tipado fuerte.. es asi el lenguaje
#puedo poner my_person_.fullname = 666
#para cambiar el __name debo crear un set
#lo correcto seria que todo fuese privado.




