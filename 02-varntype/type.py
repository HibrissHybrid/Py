#Tipos de Datos.

from typing import TextIO


nada = None
cadena = "hola soy una cadena de texto"
cadena = "developer"
entero = 99
flotante = 8.9
boleano = True #two type of data true or false
lista = [10, 20, 30, 40, 100, 200]
listaString = [10, "veinte", 30, "cuarenta"]
tupleNoChange = ("te", "vale", "vrg")  #tuplas no cambia el dato.
diccionario = {
    "name": "hibran",
    "lastname": "hybrid",
    "nickname": "hibriss"
}  # una variable con varios datos.

rango = range(9) # rango de (0-9)
dato_byte = b"provando" # tipo de dato byte. 

# imprimir variable
print(dato_byte)

# mostrar tipo de dato
print(type(dato_byte))


# Cambiar el tipo de dato a una variable

texto = "hola soy un texto"
numerito = str(777)  

print (type(numerito))

# 888  es int
# "888" es str
print(texto + " " + numerito)


numerito = int(777)  #integer  int  tipo (entero)
print(type(numerito))

numerito = float(777)  #float tipo flotante (decimal)
print(type(numerito))
