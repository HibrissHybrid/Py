"""  
# Ejercicio 3
escribir un programa que muestre los cuadrados 
(un numero multiplicado por si mismo) de los primeros
numeros reales, resuelvelo con for y while.

"""
"""
# while

count = 1 # contador
while count <=61:   # mientras contador sea menor o igual a 61
    squere = count*count # operacion del cuadrado.
    print(f"el cuadrado de {count} es {squere}")  # imprime por pantalla.
    count += 1
"""

# FOR

for num in range(61):  #num en rango al 61
    sqr= num*num  # operacion del cuadrado
    print(f"el cuadrado de {num} es {sqr}")  # imprime por pantalla  