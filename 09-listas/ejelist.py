"""
Ejercicio 1:
Escribir un programa que almacene las asignaturas de un curso
 (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
  en una lista y la muestre por pantalla.
"""

Asignaturas = ["Matemáticas", "Física", "Química", "Historia y Lengua"]
print(Asignaturas)

print("\n")  # salto de linia

"""
Ejercicio 2:
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>,
donde <asignatura> es cada una de las asignaturas de la lista.
"""

Asignaturas = ["Matemáticas", "Física", "Química", "Historia y Lengua"]
for asignatura in Asignaturas:
    print("yo estudio : " + asignatura)


print("\n")  # salto de linia

"""
Ejercicio 3:
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura,
y después las muestre por pantalla con el mensaje En <asignatura>
has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista
y <nota> cada una de las correspondientes notas introducidas por el usuario

imprime un promedio de la calificacion 

comprueba si acredito o no,  nota >= 6.


Asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
calificacion = []
for asignatura in Asignaturas:
    cali = int(input("¿Qué nota has sacado en " + asignatura + "?: "))
    calificacion.append(cali) # aqui se anade una calificacion a cada materia
print("\n")
for i in range(len(Asignaturas)):  # i en rango de cuantas asignaturas hay.
    print("En " + Asignaturas[i] + " has sacado " + str(calificacion[i])) # imprime el mensaje y las calificaciones.

print("\n")

nota = sum(calificacion)/len(calificacion)  # operacion de las notas(caloificacion)
print(f"tu calificacion es: {nota}") # imprime tus notas

print("\n")

# aqui comprobaremos si pasas a siguiente ano o tenmdrias que recursar en caso de tener una calificacion reprobada.
if nota >= 6:
    print("Felicidades Acreditaste.")
else:
    print("lo sentimos creditos insuficientes.")

"""

"""
Ejercicio 4:
Escribir un programa que pregunte al usuario los números[5] ganadores
de la lotería primitiva, los almacene en una lista y los muestre 
por pantalla ordenados de menor a mayor.
"""

winumber = []  # creamos una lista vacia
for x in range(5):  # x en un rango de 5 "5 numeros" 
    winumber.append(int(input("Introduce un número ganador: ")))  # pregunta al usuario sobre los numeros
winumber.sort()  # ordena la lista de numeros
print("Los números ganadores son " + str(winumber))  # imprime la lista de numeros.

print("\n")

"""
Ejercicio 5:
Escribir un programa que almacene en una lista los números del 1 al 10 
y los muestre por pantalla en orden inverso separados por comas.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    # creamos la lista
numbers.reverse()  # numeros inversos
for number in numbers:  # bucle de numero en numeros
    print(number, end=", ")  # imprime numeros seguidos de una coma ,,



"""
Ejercicio 4:
hacer un programa que muestre mayor y menor elemeneot de una lista predeterminada.
en una tupla.
"""

precios = [50, 75, 46, 22, 80, 65, 8] # creamos la tupla
min = max = precios[0] # minimo = max = precios=0
for precio in precios:  # precio en precios (para cada elemento)
    if precio < min:  # si precio < min
        min = precio  # min = precio
    elif precio > max: #si no, precio es mayor.
        max = precio  # precio mayor
print("El mínimo es " + str(min))  # imprime en str el precio.
print("El máximo es " + str(max))