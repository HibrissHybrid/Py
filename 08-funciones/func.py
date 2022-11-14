"""

Funciones.
una funcion es un conjunto de instruncciones agrupadas bajo un nombre 
concreto que pueden reutilizar invocando a la funcion tantas veces 
como sea necesario.



def namefuntion(parametros):
    # bloque / conjunto de instrucciones

namefuntion(funcion_parametros)
namefuntion(funcion_parametros)


"""

#EJEMPLO 1

print("##### EJEMPLO 1 #####")

"""
en este primer ejemplo creamos una funcion 
que muestre en pantalla un listado de nombres de personas 
utlizando print.
"""

def muestraNombre():
    print("hibran")
    print("Veronica")
    print("Raquel")
    print("Mariana")
    print("Nereyda")
    print("Diego")
    print("\n")

# Invocar una funcion
muestraNombre()   #nombre de la funcion entre parentesis. "sin puntos"


# EJEMPLO 2
print("##### EJEMPLO 2 #####")


"""
esta funcion no pedira el parametro al usuario,
si no que se introducira directamente en la funcion
del codigo


def mostrarTuNombre(nombre):
    print("Tu Nombre es: {nombre}")

mostrarTuNombre("hibran larreta")
mostrarTuNombre("gestor de datos")
mostrarTuNombre("alternativa alterada.")


en este ejemplo le pasamos a la funcion un parametro nombre.

def mostrarTuNombre(nombre):
    print(f"Tu Nombre es: {nombre}")
nombre = input("introduce tu nombre: ")
mostrarTuNombre(nombre)


en este ejemplo introducimos 2 parametros en una funcion, que muestra tu nombre y edad

def mostrarTuNombre(nombre, edad):
    print(f"Tu Nombre es: {nombre}")

    if edad >= 18:
        print(f"{nombre}, es mayor de edad")
    else:
        print(f"{nombre}, es menor")


nombre = input("introduce tu nombre: ")
edad = int(input("introduce tu edad: "))
mostrarTuNombre(nombre, edad)




# EJEMPLO 3
print("##### EJEMPLO 3 #####")

# una funcion que muestre la tabla
#  de multiplicar de cualquier numero que introdusca el usuario.

def table(numero):  # declarar la funcion tabla
    print(f"tabla de multiplicar del {numero}")   # mostar por pantalla
    
    for count in range(1,11):  # bucle de la tabla de multiplicar
        operacion = numero*count  #operacion 
        print(f"{numero} x {count} = {operacion}")  # tabla que mostrara en pantalla

    print("\n") # salto de linia
numero = int(input("que numero de tabla quieres: "))  #introduzca el numero
table(numero)  # invocamos la funcion.


# EJEMPLO 3.1
print("##### EJEMPLO 3.1 #####")


def table(numero):    # creamos la funcion
    print(f"tabla de multiplicar del {numero}")

    for count in range(1,11):
        opera = numero*count
        print(f"{numero} x {count} = {opera}")

    print("\n")

table(6)  # invocamos la funcion table con el parametro asignado. osea la tabla del 6.



print("---------------------------------------------------")
# ejemplo 3.1.1
# lo que haremos es crear un bucle para que nuestra funcion reciba losm parametros del bucle.
for num_table in range(1,11):   # aqui creamos un bucle con rango del 1 al 10 
    table(num_table)  #invocamos nuestra funcion con el bucle que creamos arriba.


"""

# EJEMPLO 4
print("##### EJEMPLO 4 #####")
# parametros opcionales.
# basicamente si se indica un parametro dentro de la funcion me lo mostrara si no, NO.
def getEmpleado(nombre, id = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    
    if id != None:
        print(f"id: {id}")
    
getEmpleado("hibran hybrid", 444444)


print("------------------------------")

# Ejemplo 5. return o  devolver datos.
print("\n##### EJEMPLO 5 #####")

def saludame(nombre):  # definimos una funcion que nos saludara(osea devolvera un saludo)
    zaludo = f"nice to meet u, {nombre}"  #definimos el saludo, y agregamos un parametro nombre.

    return zaludo   # return saludo.

print(saludame("hibran le.."))  # aqui invocamos la funcion y agregamos un parametro, que en este caso seria nuestro nombre

print("------------------------------")

# Ejemplo 6. return o  devolver datos.
print("\n##### EJEMPLO 6 #####")

def calculo(num1, num2, basic = False):
    #creamos las variables y su operacion
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    divicion = num1 / num2

    cadena = ""   # cadena de caracteres string.

    #cadena + operador: concatenacion de numero trasformado
    #a string  para poder imprimir el resultado.

    if basic != False:  # si basic es diferente me mostrara 
       cadena += "\nSuma: " + str(multi)
       cadena += "\nResta: " + str(divicion)

    else: # si el parametro es false.
       cadena += "\nMultiplicacion: " + str(multi)
       cadena += "\nDivicion: " + str(divicion)

    #aqui devolvemos la variable cadena

    return cadena
"""
  Aqui invocamos la funcion con los parametros 5 y 10.
   //  y el parametro true para que me imprima operaciones basicas.
"""
print(calculo(5,10, True))  

    

print("------------------------------")

# Ejemplo 7. Funciones dentro de otras funciones.
print("\n##### EJEMPLO 7 #####")

def getNombre(nombre):   # creamos funcion nombre
    texto = f"El nombre es: {nombre}"
    return texto

def getApellido(Apellido):  # creamos funcion apellido
    texto = f"El apellido es: {Apellido}"
    return texto

def devuelveTodo(nombre, apellido):  # funcion que nos devolvera 2 funciones (que estan dentro de "devuelveTodo")
    texto = getNombre(nombre) + "\n" + getApellido(apellido)   # texto es igual a la funcion de nombre +(concatenacion) funcion apellido.
    return texto  # devolvemos texto

print(devuelveTodo("Hibran", "Larreta")) # invamos la funcion con los parametros de nombre y apellido.



print("------------------------------")

# Ejemplo 8. Funciones lambda
# una funcion anonima que funiona para tareas simples.
print("\n##### EJEMPLO 8 #####")

dime_el_year = lambda year: f"el ano es {year}"
# se define en una sola linea y es corta.
print(dime_el_year(2022))

