import random    # modulo random la maquina da un numero random.

def run():   # defina la funcion
    numero_aleatorio = random.randint(1, 100)   #definimos numero aleatorio con el modulo random. random.randint(1,22) rango.
    numero_elegido = int(input("Elige un numero entre el 1 y el 100: "))  # pedimos un numero al usuario
    while numero_elegido != numero_aleatorio: # si numero elegido es difetrente de numero aleatorio
        if numero_elegido < numero_aleatorio:  # numero eleggido menor a numero aleatorio.
            print("Elige un numero mas grande")   # imprime
        else:
            print("busca un numero mas pequeno")
        numero_elegido = int(input("Elige otro numero:  "))   # para que el usuario eliga otro numero en caso de que se equivoque.
    
    print("GANASTE ALV")
if __name__ == '__main__':
    run()