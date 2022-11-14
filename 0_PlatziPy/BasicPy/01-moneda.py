# crea un convertidos de pesos a dolares

"""
logica del problema:
tenemos que saber cuantos pesoa a dolares se quiere cambiar...
asi que preguntamos 

1.cuantos pesos tienes ? 
2. dividimos pesos entre valor de dolar
3. valor del dolar mx esta en 20 pesos a dolar
4. son vslores tipo float y se representa a str para poderse concatenar con el texto.
"""

pesos = input("cuantos pesos tienes?: ")  # cuanto se quiere cambiar
pesos = float(pesos) #convertimos tipo float nuesra variable pesos
valor_de_dolar= "20.00"  # le damos valor al dolar
valor_de_dolar= float(valor_de_dolar) # volvemos float nuestra variable valor de dolar 
dolares = pesos / valor_de_dolar #hacemos la operacion pesos sobre dolar
dolares = round(dolares, 2)  # aqui queremos solo dos decimales
dolares = str(dolares) # convertimos dolares a str para poderlo concatenar
print("tu tienienes "+ dolares +" en tu bolcillo ") # imprimimos tu resultado. 