"""
 Ejercicio 8. hacer un programa que te muestre el porcentaje de un numero.
 ingresando tanto numero como porcentaje
     por ejemplo el "20% de 150" 

"""

numero = int(input("introduce un numero: "))
porcentaje = int(input(f"introduce un porcentaje quiere saber de {numero}?: "))

operacion = (numero * (porcentaje/100))


print(f"El {porcentaje}% de {numero} es:  {operacion}")

