"""
Ejercicio 1.
*Hacer un programa que tenga una lista 
de 8 numerios enteros y haga lo siguiente:
(hecho) - Recorrer la lista y mostrarla
(hecho) - hacer funcion que recorra listas de numeros y devuelva un string.
(hecho) - ordenarla y mostrarla
(hecho)- mostrar longitud
- buscar algun elemento (que el usuario pida por teclado.)
"""

# crer una lista:

numeros = [12, 64, 54, 76, 21, 7, 91, 63]

# crear una funcion que recorra la lista y devuelva un string
def mostrarLista(lista):   # creamos la funcion de mostrarlistra
    resultado = ""   # resukltrado convertido a string.

    for elemento in lista:  # recorrer los elementos
        resultado += "elemento: " + str(elemento)  # operacion a resultado valor que se devolvera.
        resultado += "\n"  # salto de linia

    return resultado  # devolvemos el resultado



# recorrer y mostrar
print("###recorrer y mostrar####")
"""
for numero in numeros:
    print(numero)
"""

print(mostrarLista(numeros))  # invocamos la funcion lista de numeros
print(mostrarLista(["hibran", "hybrid", "kakei"]))  # creamos otra lista con otros elementos ingresados en el parametro de la funcion.



# ordenar y mostrar
print("### ordenar y mostrar####")

numeros.sort()  #funcion que ordena de mayor a menor una lista.
print(mostrarLista(numeros))




# mostrar longitud.
print("### mostrar longitud. ####")

print("total de elementos en la lista son: ")
print(len(numeros))





# Busqueda en la lista
print("### Busqueda en la lista ####")

busqueda = int(input("introduce el numero a buscar: "))

comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
    busqueda = int(input("introduce el numero a buscar: "))
else:
    print(f"has introducido vel {busqueda}")

print(f"buscar en la lista el numero {busqueda}")

search = numeros.index(busqueda) # index va a buscar el valor en numero y regresara si es true or false en search
print(f"el numero buscado en la lista, es el indice: {search}")
