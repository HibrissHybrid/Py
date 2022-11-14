from ast import Continue


def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):  # RANGO DEL CICLO
        if i == 1 or i == numero:   # CUANDO LA CONDICION SE CUMPLE SALTA LA OPERACION
            Continue 
        if numero % i == 0:   # CUANDO DA 0 ES PORQUE SE DIVIDE EXACTAMENTE, Y ES COMPUESTO
            contador += 1  # SI HAY UN DIVISOR CONTADOR AUMENTA 1.
    if contador == 0:   # SI HAY RECIDUOS EN TODAS LAS DIVICIONES SABEMOS QUE ES PRIMO.
        return True  # TRUE PORQUE SI ES PRIMO
    else:  
        return False   #ES COMPUESTO PORQUE NO HAY RESIDUOS EN ALGUNA OPERACION.


def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):  # TRUE
        print('Es primo')
    else:    # FALSE
        print('Es Compuesto')


if __name__ == '__main__':
    run()