"""
Ejercicio 4. 
crear un script que tenga 4 variables, una lista, un string, 
un entero, y un booleano y que te imprima un mensaje
segun el tipo de dato de cada variable. usar funciones.
"""


def traducirTipo(tipo):  
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE CARACTERES"
    elif tipo == int:
        result = "ENTERO"
    elif tipo == bool:
        result = "BOOLEAN"
    else:
        result = "AQUI YA NO ES NADA CARNAL AQUI YA VALIO MAKANA TU PROGRAMA"
    
    return result

"""
creamos una funcion "traducirTipo" que traduca nuestra comprobacion de una variable  
"""


def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""

    if test:
        result = f"este dato es del tipo {traducirTipo(tipo)}"
    else:
        result = "este dato no corresponde"
    
    return result

"""
esta funcion comprueba el tipoi de dato de una variable con "isinstance" con parametros dato tipo.
"""


# Variables a comprobar
mi_lista = ["hola mundo", 77]
titulo = "Master en python"
numero = 102
verdadero = True


# invocamos a la funcion e ingresamos los parametros a comprobar de nuestras variables.

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))
