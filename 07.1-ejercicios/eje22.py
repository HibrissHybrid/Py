"""
Escribir un programa que pregunte al usuario por el número de horas
trabajadas y el coste por hora.
Después debe mostrar por pantalla la paga que le corresponde.
"""

horas = float(input("Horas trabajadas a la semana:  "))
coste = float(input("ganancias por hora: "))
print("\n")
print(f"Tu Ganancia Semanal es De: ({horas*coste})")

"""
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = horas * coste
print("Tu paga es", paga)
"""
