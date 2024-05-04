name = input("Como te llamas?") # ejercicio 2
print("Hola", name.title())
print(name.upper()) #ejercicio 4

edad = 29
txt = "Mi nombre es Lorena, y tengo{}"
print(txt.format(edad)) # ejrcicio 5

import random 
print(random.randrange(0,10)) #ejercicio 6

a = 20 #ejercicio 7
b = 10
print("suma", a + b)
print("resta", a - b)
print("multiplica", a * b)
print("division", a / b)
print("modulo", a % b)

r = 3 # ejercicio 8
d = 6
pi = 3.14

promedio = 2 * pi * r
area = pi * r**2

print("promedio:", promedio)
print("area:", area)

a = 5 # ejercicio 9
b = 4
c = 6
d = 2

promedio = (a + b + c + d) / 4
suma = a + b + c + d
divide = suma / 4
print("promedio:", promedio)
print("suma:", suma)
print("divide:", divide)

centimetros = float(input("Ingrese la longitud en centímetros: ")) # ejercicio 10
pulgadas = centimetros / 2.54
print("{} centímetros equivalen a {:.2f} pulgadas.".format(centimetros, pulgadas))




