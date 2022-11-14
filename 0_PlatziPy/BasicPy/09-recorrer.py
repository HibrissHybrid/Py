def run():
    #nombre = input("escribe tu nombre:  ")   # pide un nombre
    #for letra in nombre:  # letra toma cada caracter de la palabra nombre...
    #    print(letra)  # y la imprime letra x letra.

    frase = input("escriba una frase:  ") # ingresamos una frase
    for caracter in frase:   # toma cada caracter de la frase.
        print(caracter.upper())   # imprime cada caracter en MAYUSCULAS.



if __name__ == '__main__':
    run()
