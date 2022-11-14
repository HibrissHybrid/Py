nombre = "hibran Le."



#Funciones generales.
"""
Type: me define el tipo de mi variable. 
en este cxaso estamos imprimiendo print con una variable nombre
que nos imprimira el nombre.
"""

print(type(nombre)) 
###################################################

# Detectar el Tipado.

"""
La Funcion isinstance identifica si es el tipo de dato que asignemos en el segundo parametro,
en este caso queremos comprobar si la variable nombre es un str(cadena de texto"string")
"""

comprobar = isinstance(nombre, str)  # comprobamos si "nombre" es "str"
if comprobar:  # si comprobar es true, 
    print(f"{nombre}, es una cadena de texto (str)")
else:  # si no se cumple.
    print(f"{nombre}, NO es una cadena de texto (str)")

if not isinstance(nombre, float):    # si no es nombre con float.
    print(f"{nombre}, no es un numero con decimales.")  # la variable "noimbre", no es un numero con decimales.


########################################################

# Limpiar espacios

"""
frase = "   mi contenido    "
frase guarda una cadena de caracteres
que tiene muchos espacios estre su mensaje

.strip() ,  es una funcion que elimina 
todos los espacios de MAS de una cadena de caratera

"""

frase = "   mi contenido    "

print(frase)
print(frase.strip())   # frase.strip  = "mi contenido"


#####################################

# Eliminar Variables.

"""
la funcion "del" la usamos para eliminar variables.
"""

year = 2021  # creo una variable
del year  # la elimino
# print(year)  al imprimir la variable por pantalla me muestra que no esta definida.

########################################

# comprobar si una variable esta vacia.
"""
la funcion "len" puede leer caracteres o numeros.
"""

texto = " ff.  "

if len(texto) <= 0:
    print("texto, estavacio.")
else:
    print("texto tiene contenido: ", len(texto))  # en este caso contara cuantos caracteres tiene la variable texto en este caso son 6.


########################################

# Encontrar caracteres 

"""
.find(parametros_de_busqueda)    // seguido de la variable

imprime el caracter que busca el usuario.    en este caso la palabra todo.
"""

texto1 = "puedes con todo, pero no con todo a la vez."
print(texto1.find("todo"))  

##########################################

# remplazar palabras en un string.
"""
.replace("O.G","G.SHIT") // despues de la variable, cambiara los parametros asignados.
"""

nuevo_texto = texto1.replace("todo", "la caca")  # remplaza "todo"  por  "la caca"
print(nuevo_texto)  # imprime la nueva frase con los parametros ya cambiados.

##############################
# mayusculas y minusulas

"""
.lower()  // minusculas el texto.
.upper()  // mayusculas el texto.
"""

name = "hibran larreta"

print(name.lower())
print(name.upper())

########################

