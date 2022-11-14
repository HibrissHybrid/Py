"""
curiosidades para hacer mas eficiente una funcion


preferentemente:
1.- el codigo de las funciones preferentemente van hasta arriba del codigo.
2.- la funcion puede acceder a variables globales(fuera de la funcion) , si se declaran antes de imprimir la funcion
"""

def mi_funcion(nombre):  #pasando parametros
    return "hola que tal" + nombre

def mi_segunda_funcion(apellido):
    return "hola que tal" + apellido

nombre = "hibran"    # se declara la variable antes de...
apellido = "larreta"

print(mi_funcion(nombre))   # ... imprimir/invocar a la funcion.
print(mi_segunda_funcion(apellido))  # y pasando el parametro de la funcion ya definida.