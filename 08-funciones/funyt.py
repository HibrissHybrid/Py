"""
Creare un programa que te imprima la puntuacion se una clase
con cierta cantidad de alumnos.

la funcion "sum"  sumara todos los elemtosNumericos que esten en la variable (puede ser listas o tuplas.)

"""

def puntuacion(clase):  #  definimos una funcion
    return sum(clase) / len(clase)  # regresamos el promedio de la clase suma todos los elementos de la clase / la cantidad de elementos en clase.

clase = [7, 10, 6]  # clase con 3 puntajes
media = puntuacion(clase)  # puntuacion toma los parametros de clase.
print(f"la puntuacion de la clase es: {media}")  # imprime por pantalla la puntuacion 

clase = [6, 5, 6, 8]  # aqui creamos una clase con 4 puntuaciones.
media = puntuacion(clase)  # puntuacion toma los parametros de clase.
print(f"la puntuacion de la clase es: {media}")   # imprime por pantalla la puntuacion 


############################################
# programa en funcion de tabla de multiplicar.

numero = int(input("numero de la table: "))  # pedir el numero de la tabla para mostrar,

def tabladel(num, lin):   # funcion "tabla del"   parametros "numero, linea"
    print(num, "x", lin, "=" ,num*lin)  #funcion que se mostrara en pantalla segun parametros.

tabladel(numero, 1)
tabladel(numero, 2)
tabladel(numero, 3)
tabladel(numero, 4)
tabladel(numero, 5)
tabladel(numero, 6)
tabladel(numero, 7)
tabladel(numero, 8)
tabladel(numero, 9)
tabladel(numero, 10)

################################################################