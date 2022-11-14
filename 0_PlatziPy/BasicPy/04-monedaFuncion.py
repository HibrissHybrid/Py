def conversor(pais_pesos, valor_dolar): #parametros el moneda del pais, y su valor del dolar.

    pesos = input("cuantos pesos" + pais_pesos + " tinenes: ")  # preguntamos pesos tiene. 
    pesos = float(pesos)    # convertimos el tipo de dato a float
    dolares = pesos / valor_dolar #operacion pesos a dolares
    dolares = round(dolares, 2) #reducimos decimales a solo 2.
    dolares = str(dolares)  #convertimos dolares a caddena de texto
    print("tu tienienes "+ dolares +"  en tu bolcillo ") #imprimimos el resultado a dolares. 


menu = """
Bienvenido al conversor de monedas multipais

1-Pesos Mexicanos 20.00 pesos
2-Pesos Colombianos 3715.00 pesos
3-Pesos Argentinos 71.00 pesos 

Elige una opción: 

"""
opcion = int(input(menu))

if opcion == 1:  # pesos mexicanos
    conversor("mexicanos", 20.00)   # imprimimos la funcion con los parametros pais y el valor de dolar. 
elif opcion == 2:  # pesos Colombianos
    conversor("colombianos", 3715.00 )
elif opcion == 3:
    conversor("colombianos", 71.00)    
else:
    print("elije un numero, paro")
