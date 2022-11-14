"""
 Funciones predefinidas en el tema de listas en Python
"""

cantantes = ['2pac','drake','bad bunny','julio iglesias']
numero = [1,2,5,8,3,4]

# Ordenar listas numnericas
print(numero)  # imprime lista desordenada
numero.sort()  # .sort() funcion que ordena de menor a mayor una lista numerica
print(numero)  # imprime lista ordenada


print("\n")  # salto de linia


# Anadir elementos
cantantes.append("tungas")   # .append anade elemento a la lista "que queda hasta el final"
cantantes.insert(0, "el cuarteto de nos")  # .insert   indicamos que el nuevo elemento tomara la posicion "0" de la lista
#print(cantantes)  # imprime la lista de cantantes con las modificaciones realizadas.

# eliminar elementos.
cantantes.pop(1)  # .pop() elimina el indice que se indique en el parametro
cantantes.remove('bad bunny')  # elimina a bad bunny de la lista
#print(cantantes)

# dar la vuelta
print(numero) #antes del reverse
numero.reverse()  # .reverse  pone de reversa la lista de numeros. 
print(numero)  # despues del reverse

# Buscar dentro de una lista
print('drake' in cantantes)

#contar elementos de una lista.
print(cantantes)
print(len(cantantes))  # .len()  cuenta cuantos elementos tiene una lista o una cadena de caracteres.

# cuantas veces aparece un elemento (frecuencia)
numero.append(8)  # agregamos un "8" a nuestra lista para asi tener 2
print(numero.count(8))  # .count() , me cuenta la frecuencia de un elemento que le pase por parametros,


# Conseguir Indice
# en este caso usamos .index() ,  para ubicar un elemento en la lista y nos diga en que posicion esta.
print(cantantes.index("drake"))  # en este caso esta en la posicion 1.



# como unir listas
""" Comom unir dos listas, .extend(lista)

en este caso los elementos de "numero" se anadieron a cantantes
['el cuarteto de nos', 'drake', 'julio iglesias', 'tungas', 8, 5, 4, 3, 2, 1, 8]
"""
cantantes.extend(numero)

print(cantantes)


