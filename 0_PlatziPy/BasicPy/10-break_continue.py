from ast import Break
from concurrent.futures import BrokenExecutor


def run():
    # imprime los numeros pares. de 2 en 2.

    #for contador in range(1000):
    #    if contador % 2 = 0:  # aqui falta poner diferente de 0. =/
    #        continue
    #    print(contador)

    # ciclo for interrumplido por un break.  como se indica en el codigo.
    #for i in range(1000000):
    #    if i == 534564:
    #        Break

    texto = input("Escriba un texto: ")   # pide un texto
    for letra in texto:  # recorrer caracteres 
        if letra == 'o':  # si el recorredor es igual a o, 
            break  # se para el programa. queda en break.
        print(letra)   #imprime letra.

if __name__ == '__main__':
    run()