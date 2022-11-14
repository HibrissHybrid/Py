menu = """
Bienvenido al conversor de monedas multipais

1-Pesos Mexicanos 20.00 pesos
2-Pesos Colombianos 3715.00 pesos
3-Pesos Argentinos 71.00 pesos 

Elige una opción: 

"""

# creo un menu de opciones
# de derecha a izquierda: llamo a la funcion input, le paso la variable menu para que la imprima y reciba el número que el usuario escogió, lo convierto a int y lo guardo en la variable 'opcion'
opcion = int(input(menu))

if opcion == 1:  # pesos mexicanos
   pesos = input("cuantos pesos Mexicanos tienes?: ")  # cuanto se quiere cambiar
   pesos = float(pesos) #convertimos tipo float nuesra variable pesos
   valor_de_dolar= "20.00"  # le damos valor al dolar
   valor_de_dolar= float(valor_de_dolar) # volvemos float nuestra variable valor de dolar 
   dolares = pesos / valor_de_dolar #hacemos la operacion pesos sobre dolar
   dolares = round(dolares, 2)  # aqui queremos solo dos decimales
   dolares = str(dolares) # convertimos dolares a str para poderlo concatenar
   print("tu tienienes "+ dolares +"  en tu bolcillo ")

elif opcion == 2:  # pesos Colombianos
   pesos = input("cuantos pesos Colombianos tienes?: ")  # cuanto se quiere cambiar
   pesos = float(pesos) #convertimos tipo float nuesra variable pesos
   valor_de_dolar= "3715.00"  # le damos valor al dolar
   valor_de_dolar= float(valor_de_dolar) # volvemos float nuestra variable valor de dolar 
   dolares = pesos / valor_de_dolar #hacemos la operacion pesos sobre dolar
   dolares = round(dolares, 2)  # aqui queremos solo dos decimales
   dolares = str(dolares) # convertimos dolares a str para poderlo concatenar
   print("tu tienienes "+ dolares +" en tu bolcillo ")
   
elif opcion == 3:  # pesos argentinos
   pesos = input("cuantos pesos tienes?: ")  # cuanto se quiere cambiar
   pesos = float(pesos) #convertimos tipo float nuesra variable pesos
   valor_de_dolar= "271.00"  # le damos valor al dolar
   valor_de_dolar= float(valor_de_dolar) # volvemos float nuestra variable valor de dolar 
   dolares = pesos / valor_de_dolar #hacemos la operacion pesos sobre dolar
   dolares = round(dolares, 2)  # aqui queremos solo dos decimales
   dolares = str(dolares) # convertimos dolares a str para poderlo concatenar
   print("tu tienienes "+ dolares +" en tu bolcillo ")
else:
    print("elije un numero, paro")