"""
ejercicios con cadenas stgring str

hacer un programa que pida al usuario su nombre y un numero n e imprima el nombre n veces.

"""

nombre = input("como te llamas? ")
n = int(input("introduce un numero: "))

print((nombre + "\n") * int(n))


# lo que pasa es que multiplicara por n su nombre y lo imprimira por pantalla, 
# agrewgamos un \n para pasarnos a otro renglon y que no escriba todo sobre la misma linia.