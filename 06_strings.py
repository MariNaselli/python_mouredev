#Strings

my_string = "My String"
my_other_string = "My Other String"

print(len(my_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de línea"

print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"

print(my_tab_string)

my_scape_string = "\tEste es un string\ncon scape"

print(my_scape_string)

#Formateo

name, surname, age = "Mariana", "Naselli", 36

print("Mi nombre es {} {} y mi edad es {}".format(name, surname,age))

print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language

print(a)
print(b)

#División

language_slice = language[1:3] #lo que esta entre... 

print(language_slice)

language_slice = language[1:] #desdde... 

print(language_slice)

language_slice = language[-2]

print(language_slice)

reversed_language = language [:: -1] #reves
print(reversed_language)

#Funciones

print("---------------")

print(language.capitalize())
print("---------------")
print(language.upper())
print("---------------")
print(language.count("t"))
print("---------------")
print(language.isnumeric())
print("---------------")
print(language.lower())
print("---------------")
print(language.lower().islower())
print("---------------")
print(language.startswith("py"))
print("---------------")
print(language.lower())
print(language.startswith("Py"))
print(language)