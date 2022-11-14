"""
# Ejericio 6
programa que muestre las tablas de multiplicar del 1 al 10
mostrando el titulo y las multiplicaciones.

"""

# solo se mostraran las tablas del 1 al 10, como lo indica el rango.

for head in range(1,11):
    print("#####################")
    print(f"#### Tabla del {head} #####")
    print("#####################")   # esta es la cabecewra del trograma

    for num in range(1,11):  # aqui hacemos el rango de las operaciones
        print(f"{num} X {head} = {num*head}") # hacemos la operqacion e imprimime el resultado.

    print("\n")

