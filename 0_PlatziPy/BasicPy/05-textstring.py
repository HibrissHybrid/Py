"""
La consola interactiva de python. 
.... abre simbolo de sistema y ejecuta el comando "py" 




>>> nombre = input("cual es tu nombre ? :  ")    # pedimos un nombre
cual es tu nombre ? :  facundo    
>>> nombre   # imprimimos el nombre
'facundo '        
>>> nombre.upper()   # .upper() es una funcion que rescribe en MAYUSCULAS
'FACUNDO '
>>> nombre.capitalize()  #.capitalize()  rescribe el nombre con la primer letra Mayuscula.
'Facundo 
>>> nombre = nombre.capitalize()   # asi dejamos guardada la funcion en nombre
>>> nombre
'Facundo '
>>> nombre = nombre.strip()  #.strip()  quita los espacios que halla en el texto.
>>> nombre
'Facundo'
>>> nombre = nombre.lower()  #.lower()  convierte el texto en minusculas
>>> nombre
'facundo'
>>> nombre = nombre.replace('o','a')  #.remplace()   remplaza letras segun lo indiques en los parametros
>>> nombre
'facunda'
>>> nombre[0]  # me indica el primer/cero caracter de mic adena de texto.
'f'
>>> letra = nombre[2]  # guardara el caracter de esa posicion de nombre "c"
>>> letra
'c'
>>> len(nombre) # len  funcion para contar los caracteres en una cadena de texto.
7
>>> len(letra)
1

"""

"""
>>> nombre = "Francisco"
>>> nombre
'Francisco'
>>> nombre[2]  # seleciona el carcter de la seunda posicion
'a'
>>> nombre[0:3]  #tomara solo los elementos de 0 al 3
'Fra'
>>> nombre[:3]  # tomara los telementos del 0 al 3 
'Fra'
>>> nombre[1:7]   # tomara los elementos del 1 al 7.
'rancis'
>>> nombre[1:7:2]  # tomara los elementos del 1 al 7 de dos en dos.
'rni'
>>> nombre[::]  #toma todos los carcateres de mi texto.
'Francisco'
>>> nombre[1::3]  #toma del 1 al final de tres en tres.
'rcc'
>>> nombre[::-1]   # toma todos los elementos alrrevez. 
'ocsicnarF'
>>>

"""