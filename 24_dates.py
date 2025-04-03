"""
dates => datetime modulos relacionados con fechas
importando el modulo

"""

#import datetime

#now = datetime.datetime

from datetime import datetime

now = datetime.now()

print(now)
print("-------")
print(now.month)
print("-------")
print(now.year)
print("-------")
print(now.day)
print("-------")
print(now.hour)
print("-------")
print(now.minute)
print("-------")
print(now.second)
print("-------")

timestamp = now.timestamp()
print(timestamp) #forma de convertirla?? es el justo momento con que se corresponde
#es algo fijo.. podemos transformarlo despues--

print("-------")

#que pasa si quiero definir la fecha/trabajar con una fecha

print("##############")

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

#print_date(now)

year_2026 = datetime(2026, 1, 1, 3)

print_date(year_2026)

print("................")
from datetime import time

current_time = time()

print(current_time.hour)
print(current_time.minute)
print(current_time.second)



