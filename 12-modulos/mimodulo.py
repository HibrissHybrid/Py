
# funcion saludo.

def holamundo(nombre):
    return f"hola mundo que tal estais, {nombre}"


# funcion calculadora

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