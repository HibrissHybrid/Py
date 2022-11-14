"""
Variables locales: se definen dentro de la funcion
y no se pueden usar fuera de ella, solo estan disponibles dentro 
a no ser que se haga un return.

Vaiables Globales: son las que se declaran fuera de una funcion 
y estan disponibles dentro y fuera de ellas.

"""

# Variables Globales.
frase = "un mar en calma nunca hizo a un marinero experto."   # ejemplo de cualquier variable global

print(frase) # imprime la frase en opantalla. (cotidianamente)

def holaMundo():   # definimos una funcion.
    frase = "hello word"  # aqui volvemos a asignarle un dato a frase, denrto de la funcion
    print("dentro de la funcion!")   # dentro de la funcion
    print(frase) # imprime frase

    year = 2021   #te pide el ano 
    print(year)  # imprime el ano.

    """
    con la palabra (global) podemos crear variables globales que se puedan usar dentro y fuera de las funciones
    """

    global website  # en esrte caso website es un variable global.
    website = "udemy.com"   # se define la variable global
    print("dentro", website)   # aqui se muestra que la variable se puede imprimir dentro de la funcion.

    return "dato devuelto " + str(year)  # RETURN, para imprimir ano, 

print(holaMundo())   # invocamos la funcion. 
print("fuera:", website)   # aqui nos damos cuenrta que nuestra variable global tambien se puede imprimir fuera de la funcion.



