"""
Escribir un programa que pregunte
el nombre completo del usuario en la consola
y después muestre por pantalla el nombre completo
del usuario tres veces, una con todas las letras minúsculas,
 otra con todas las letras mayúsculas y
otra solo con la primera letra del nombre y de los apellidos en mayúscula.
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""

nombre = input("como te llamas?: ")

print(nombre.lower())  #minusculas
print(nombre.upper()) #mayusculas
print(nombre.title()) # letra pequena

print("\n")
print("##########################################")

"""
hacer un programa que muestre cuantas letras tiene una palabra
"""

palabra = input("escribe una palabra:   ")

print(palabra.upper() + " tiene " + str(len(palabra)) + " letras")

"""
para concatenar en un print op + "palabra str" + op
str(len(palabra)) # cuenta cuantos caracteres.
"""


print("\n")
print("##########################################")



