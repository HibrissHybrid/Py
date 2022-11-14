"""
#Ejercicio 2
hacer un programa que te imprima los numeros pares e impares del 1 al 120

"""

count = 1  #contador
for count in range(1,120):  #blucle for donde creamos un rango de (1,120) 
    if count % 2 == 0:  # si contador es dividible entre 2 
        print(f"{count}, Es Par")  # si es divisible entre 2 es par
    else:   
        print(f"{count}, Es Impar")  # si no!  no es par.