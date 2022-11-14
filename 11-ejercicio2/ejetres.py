"""
ejercicio 3.
programa que recubra si una variable esta vacia
y si esta vacia, rellenar con texto en mayusculas
y mostrarlas
"""

texto = " "   # creamos una variable vacia (texto vacio,)

if len(texto.strip()) <= 0: # si texto(que se cuenta "len") es menor e igual a 0: entonces:

    texto = "hola soy un texto en mayusculas"  # rellena la variable con contenido
    print(texto.upper())  # imprime la variable con el contenido en mayusculas.
else:   # y si no
    print(f"la variable tiene contenido {texto}")   # es porque la variable tiene algun contenido.



"""
en la condicion if la funcion "len" contara cuantos caracteresw tiene nuestraq variable,
   y la funcion ".strip()"  nos borrara espacios vacios.

"""