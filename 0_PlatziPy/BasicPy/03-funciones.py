
"""
#Funciones 

Las funciones son cajas de procesos donde puedo tener valores de entrada y salida de datos 

las funciones son pedazos de codigo que realizan alguna tarea en especifico



def imprimir_mensaje():   # definir funcion():  
    print("mensaje especial !")  # dentro de la funcion ira pedazos de codigo que haga la funcion a realizar.
    print("estoy aprendiendo a usar funciones ! >3 ")

imprimir_mensaje()  # invocar/imprimir la funcion.  solo la escribimos tal cual la funcion

"""


"""
Prametros en funciones
 Aqui tenemos:
 un programa que imprime un mensaje de acorde a la opcion que elijas...


# funciones y parametros.

opcion = input("elige una opcion (1, 2, 3.): ")

if opcion==1:
    print("hola")
    print("como estas ")
    print("elegiste la opcion 1 ")
    print("adios")
elif opcion==2:
    print("hola")
    print("como estas ")
    print("elegiste la opcion 2 ")
    print("adios")
elif opcion==3:
    print("hola")
    print("como estas ")
    print("elegiste la opcion 3 ")
    print("adios")
else:
    print("elige una opcion (1, 2, 3.): ")

"""

""" 

 ******  Nuevo bloque de codigo con parametros a nuestro mensaje de opcion.

   En nuestro blque de codigo solo cambia el mensaje que 
   imprime que opcion selecionaste y la cambiaremos atra vez de tener un parametro "MENSAJE"

"""


"""
def conversacion(Mensaje):   #Aqui nuestra Funcion(conversacion) tiene un parametro llamado (mensaje)


    print("hola")      # Esta es nuestra conversacion...
    print("como estas ")
    print(Mensaje)
    print("adios")

opcion = int(input("Elige una opcion (1, 2, 3.): "))   # Aqui pediremos una opcion al usuario.

if opcion==1:  #opcion 1 si el usuario escribe uno en nuestra condicional.
    conversacion("Elegiste la opcion 1")    # Aqui invocamos nuestra funcion con el parametro "Mensaje de la opcion que eligio."
elif opcion==2:   
    conversacion("Elegiste la opcion 2")
elif opcion==2:
    conversacion("Elegiste la opcion 2")
else: 
    print("elige una opcion porfavor (1, 2, 3.): ")   # en caso de que se equivoque 
"""

"""

# imprimir parametros dentro de una funcion

#  Una funcion que devuelve la sumatoria de los parametros suma(a, b)

from pdb import Restart


def suma(a, b):   # definimos la funcion suma y los parametros a sumar.
    print("la suma de dos numeros")  # imprimir mensaje
    resultado = a + b # operacion de la suma guardandose en resultado la suma de a + b
    return resultado  # return devuelve el resultado 

sumatoria = suma(1, 4)  # el resultado toma los parametros de suma que se guarda en Sumatoria 
print(sumatoria)   # imprime la funcion que devuelve los parametros del resultado de la suma.


### a ver tuu  genial bro lo haz hecho muy bien sigue practicando tdos los dias las veces que sea necesario para ir mejorando en este pedo...
"""

def artimetico(x, y):
    print("Esta es una funcion aritmetica que devuelve las operaciones A. de dos variables")
    suma = x + y 
    resta = x - y
    multiplicacion = x * y
    divicion = x / y

    return print("la suma es: {}\n la resta es: {}\n la multiplicacion es: {}\n la divicion es: {} ".format(suma, resta, multiplicacion,divicion))
 

x = int(input("ingrese un numero x: "))
y = int(input("ingrese un numero y: "))
arit = artimetico(x, y)
print(arit)






