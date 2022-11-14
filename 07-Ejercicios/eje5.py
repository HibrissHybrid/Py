"""
# Ejercicio 5
hacer un programa que muestre todos los numeros 
que hay entre 2 numeros que ingrese el usuario,
"""

num1 = int(input("introduce 1r numero:"))
num2 = int(input("introduce 2do numero:"))

if num1 < num2:  # si el num1 es menor quee num2
    for count in range(num1,(num2 +1)):  # aqui se genera el rango directamente
        print(count) # y despues se imprime el contador.


else: # si no,
    print(f"el {num1} tiene que ser menor que {num2}") 