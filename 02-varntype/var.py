"""
Una Variable es un contenedor de informacion
que dentro guardara un dato, se pueden crear
muchas variabloes y que cada uno tenga un dato distinto
"""

# Crear variables y asignarles un valor.

#String
texto = "master en python"
texto2 = "con hibran hybrid"
#integer (int)
numero = 45
decimal = 6.7

# mostrar el valor de l;as variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("-------------------------------------------")

#sustituir el valor de algunas variables
numero = 27
decimal = 8.9  #aqui se cambia el dato mde las variables porque es lo sig, en el codigo.

print(numero)
print(decimal)

print("-------------------------------------------")

#Concatenacion

name = "hibran"
lastname = "hybrid"
email = "hibranle@gmail.com"

print(name + "-" + lastname + " - " + email)
print(F"{name} {lastname} {email}")  
print("hola me llamo {} {} y mi email es: {}" .format(name, lastname, email))

print(name, lastname, email)  #aqui no estamos concatenando solo esta imprimiendo.


nombre = input("ingresa tu nombre: ")

apellido = input("ingresa tu apellido: ")

correo = input("ingresa tu correo gmail: ")

print("hola {} {} bienvenido a la compania le enviaremos un correo a su gmail: {}" .format(nombre, apellido, correo))