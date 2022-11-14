"""
Escribir un programa que pregunte al usuario
una cantidad a invertir, el interés anual y el número de años,
 y muestre por pantalla el capital obtenido en la inversión.
"""

inversion = float(input("Cantidad a invertir: "))
interes_anal = float(input("Interes Anal: "))
anos = int(input("Cuantos Anos: "))

print("Capital final: " + str(round(inversion * (interes_anal / 100 + 1) ** anos, 2)))

"""
¿Cantidad a invertir?  1000
¿Interés porcentual anual?  10
¿Años? 5
Capital final: 1610.51
"""