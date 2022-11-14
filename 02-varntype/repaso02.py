from typing import TextIO


print("hola mundo")

"""
Una variable es un contenedor de informacion
 que dentro guardara un dato, 
 se pueden crear muchas variables y cada uno tener un dato distinto 
"""

#String  (Cadena de Texto letras y palabras)
texto = "Master en python"
texto2 = "con Hibran Hybrid"

#integer (int) 
numero = 45  #esto es el ejemplo de una variable (int) tipo entero
decimal = 6.7 #esto es el ejemplo de una variable (float) tipo flotante que representa valores de tipo decimal...

# Mostrar Valores En Pantalla
print("=================================================")

print(texto)
print(texto2)
print(numero)
print(decimal)

print("=================================================")

# sustituir el valor de una variable
#volviendo a declarar la misma variable

numero = 25
decimal = 8.9  # se sustituye el valor porque el codigo corre de arriba a abajo.

print(numero)
print(decimal)

print("=================================================")
"""

 CONCATENACION + CONCATENACION CONCATENACION + CONCATENACION CONCATENACION + CONCATENACION
  CONCATENACION + CONCATENACION CONCATENACION + CONCATENACION CONCATENACION + CONCATENACION


name = "hibran"
lastname = "hybrid"
email = "hibranle@gmail.com"

# concatena variables con texto para mostrarlas en pantalla con los datos de enetrada.

print(name + "-" + email + "-" + lastname) # de esta forma concatenamos solo texto

print(f"{name} {lastname} {email}") # f para la funcion de concatenacion de variables. al imprimir


# asi en un enunciado puedo concatenar variables de cualquier tipo a texto.
print("hola me llamo {} tengo {} y mi apellido es {} mi email es: {}" .format(name, numero, lastname, email))



name1 = input("NOMBRE: ")

last2 = input("APELLIDO: ")

email = input("EMAIL: ")

print("hola {} {} le enviamos un correo a {}".format(name1, last2, email))

""" # Variables y Concatenacion
print("=======typos de datos========")
# Tipos de Variables

nada = None #representa que esta vacio o ningun dato, inacion
cadena = "hola soy una cadena de texto"  #texto
cadena = "developer" #texto, nombre etc
entero = 99  #valores enteros
flotanteDecimal = 7.9  #valores con punto decimal
boleano = True #two type of data true or false
lista = [10, 20, 30, 40, 50, 100]
ListaString = [10, "veinte", 40, "treinta"]  #lista con cadena de texto u otras variables con tipos de datos.
tupleNoChange = ("te", "vale", "vrg")  #tuplas no cambia el dato
diccionario = {
    "nombre1": "hibran",
    "lastname2": "hybrid",
    "nickname": "hibrisshybrid"
} # un diccionario es una variable con varios datos relacionados.

#tipo de dato Rango, secuencia numerida de x-n
rango = range(9)  # rango de 0 al 9

# tipo de dato byte
dato_byte = b"provando" #tipo de dato byte


print("===================== imprimiendo tipos de variables =====")
# Imprimir variable

print(diccionario)

# Imprimir tipo de dato

print(type(diccionario))

print("===================== Cambio de tipo de variable")

# cambiar tipo de datos a variables

soytexto = "hola soy un texto"
numerito = str(888)

# 888 es int  osea entero  
# "888"  es str cadena de texto

print(soytexto + " " + numerito)  # aqui me lo va a concatenar porque sabe que numerito es un str cadena de texto.


numerito = int(777)  #integer in tipo entero 
print(type(numerito))

numerito = float(888)  #numerito ahora es tipo flotante osea decimal
print(type(numerito))


print("=======Ejercicio========")
# un programa que imprima tu nombre y tu edad cambiando int a str

nombree = input("nombree : ")
edades = input("edad : ")

edades = str(edades)

print("hola soy " + nombree + " y tengo " + edades + " nos de edad")

print("hola soy" + " " + nombree + " y tengo " + edades + " anos de edad")  

print("mi nombre es {} y mi edad es  {}".format(nombree, edades))  # aqui no importa que tipo de datos sean las variables para que se muestren en una cadena de textos.

print("===============")