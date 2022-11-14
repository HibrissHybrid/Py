"""
#  LISTAS / ARRAYS

Son coleccion o conjuntos de datos/valores, bao un unico nombre.
Para acceder a estos valores podemos usar un indice numerico.


--list(arrays)
crear una lista:

a = []   #si
b = list()  #no
a == b   # de cualquier forma se pueden crear una lista
true
   "a = [1, 2, 3, 4]" asi podrias crear una lista.



--tuple (tuplas.)

a = ()    # b = (5,)  # Es una tupla nde un solo elemento.
b = tuple()  # estas son las dos formas de crfear una tupla.
a == b
True

"""


# Definir una lista (list)

peliculas = ["lalola","enelbano","cantandopis"]  # lista de peliculas
artist = list(('drake','2pac','paja'))  # lista de artistas
year = list(range(20,50)) # lista que me de los numeros dentro de ese rango.
variada = ("hibran", 24, 1.70004, "hybrid")  #lista variada donde tenemos diferentes tipos de datos.


"""
print(peliculas)
print(artist)
print(year)
print(variada)
"""

# INDICES:

print(peliculas[0])  # esta nos imprimiria el elemento 0 de la lista en este caso "lalola"
print(peliculas[1])  # enelbano
print(peliculas[2])  # contadopis
print(peliculas[-1]) # contadopis
print(peliculas[-2]) # enelbano

print(peliculas[2:]) # solo imprimira un solo elemento seleccionado.

print(peliculas[0:2]) # me imprimira los elementos en el rango del 0 al 2 "lalola,enelbano"


print("\n")
print("########################################################")
# como cambiar un elemento de la lista:

artist[1] = "elcuarteto"    # seleccionas la variable de la lista y el elemto [n] que se necesite modificar.

print(artist)   # aqui me imprime la lista de artistas modificadas.


print("\n")
print("########################################################")
# anadir elementos a una lista.

artist.append("elkakas")  #usamos el ".append" seguido del elemento a agregar.
artist.append("rubadro") #anadimos otro elemento mas.
print(artist) 



print("\n")
print("########################################################")
# recorrer listados.

print("********** listados de peliculas *********")

"""
Programa que cree una lista de elementos.
"""

new_peli = ""   # creo una variable "new_peli" ""
while new_peli != "parar":  #while mientras sea diferente o igual que parar:
   new_peli = input("introduce una pelicula: ") #pelime una pelicula

   if new_peli != "parar":   #si new_peli es diferente igual a "parar"
      peliculas.append(new_peli) #peliculas cva a agregar una pelicula a la lista.

print("********** listados de peliculas *********")  

for pelicula in peliculas:   # un bucle que itere en peliculas
   print(f"{peliculas.index(pelicula)+1}. {pelicula}")  # me imprima la lista de elementos.



print("\n")
print("########################################################")
# listas multidimencionales.

"""listas dentro de otras listas"""

print("************* LISTAS DE CONTACTOS. ****************")

contactos = [
   [
      'andy verga',
      'andy@verga',
      '666 555 7868'
   ],
   [
      'ste men-so',
      'stemenso.con',
      '9999 888 9809'
   ],
   [
      'esta cafe',
      'estacafe.comal',
      '666 777 7876'
   ],
]
"""
print(contactos)  # si queremos imprimir toda la list de contactos.

print(contactos[1][1]) # stemenso.con

print(contactos[1][2]) # 9999 888 9809




for contacto in contactos:
   print(contacto)     # de esta manera me estaria imprimiendo todos los elementos.


for contacto in contactos:
   print(contacto[0])         # este for solo me imprimira el primer elemento de cada contacto "andy verga, ste men-so, esta cafe"



for contacto in contactos:
   for elemento in contacto:
      print(elemento)
   print("\n")     # de esta manera me estaria imprimiendo todos los elementos. de los contactos, separados por un \n
"""

for contacto in contactos:
   for elemento in contacto:
      if contacto.index(elemento) == 0:
         print("nombre: " + elemento)  # identificara el nombre del elemento
      elif contacto.index(elemento) == 1:
         print("email: " + elemento)   # identificara el email del elemento
      else:
         print("phone: " + elemento)  # identificara el phone del elemento
   print("\n") 

