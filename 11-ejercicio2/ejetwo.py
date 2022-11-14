"""
ejerciciio 2.
escribir un  programa que  anada valores a una lista 
mientras que su longuitud sea menor a 120 
y luego mostrar la lista.
plus: usar while y for


print("## FOR ##")

coleccion = []  # creamosuna lista vacia

for contador in range(0, 120):  # for para crear el rango de numeros.
    coleccion.append(f"elemento- {contador}") # agrega elemento.append
    print("Mostrar el: " + coleccion[contador]) # imprime el contador de elementos

print(coleccion[110])  # imprime hasta parametro ingresado.

"""


print("## while ##")

coleccion = []
x = 0

while x < 120: # mientras que x sea menor que 120
    coleccion.append(f"elemento-{x}")  # agregar
    print("mostrar el: " + coleccion[x]) # mostrar
    x +=1  # contador

print(coleccion[110]) # imprime hasta parametro ingresado.

