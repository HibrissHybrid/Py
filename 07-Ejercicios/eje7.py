"""
 Ejercicio 7.  hacer un programa que muestre todos los numeros 
 impares entre 2 numeros que ingrese el usuario.


"""

num1 = int(input("Introduce el 1r numero"))
num2 = int(input("Introduce el 2do numero"))

if num1 < num2:

    for x in range(num1, (num2 + 1)):   #aqui marcamos un rango entre los dos numeros que ingrese el usuario.
        if x%2 == 0:   #m operacion para identificar el par.
            print(f"{x}, es par")
        else:
            print(f"{x}, es impar")


else:
    print("El num1 debe ser mayor al num2")