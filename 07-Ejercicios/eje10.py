"""
# Ejericio 10
programa que pida las notas de 15 alumnos 
y sacar por pantalla cuantos aprobaron y cuantos reprobaron.

"""

contador = 1
aprov = 0
reprov = 0

num_alumnos = int(input("cuantos alumnos tienes?: "))  # pide al usuario la cantidad de alumnos

while contador <= num_alumnos:   # bucle while mientras contador sea <= numero de alumnos
    calif = int(input(f"calificacion del \"alumno{contador}\" ?  "))  #el usuario ingresa clificcxacion de alumno

    if calif >= 6:   # si su calificacion es mayor o igual a 6 esta aprovado
        aprov += 1  # aqui se agrega 1 a la variable aprovado
    else:   # y si noo aprovo
        reprov += 1  # se le agrega 1 al reprovado

    contador += 1  # contador de while incrementa en 1.

print(f"\n Alumnos aprovados:  {aprov}")    # print para mostar por pantalla total de aprovados y reprovados.
print(f" Alumnos reprovados:  {reprov}") 