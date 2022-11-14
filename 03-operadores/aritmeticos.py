print("OPERADORES ARITMETICOS")

# Operadores aritmeticos

numero1 = 55  # 1. entrada de datos ya sea establecidos y ingresados por el usuario
numero2 = 5

resta = numero1 - numero2   # 2. variable y operacion entre los numeros
multiplicacion = numero1 * numero2
divicion = numero1 / numero2
resto = numero1 % numero2

print("********* CALCULADORA*************")

print(f"la suma es: {numero1 + numero2}")  # aqui hacemos la suma directamente
print(f"la resta es: {resta}")
print("La multiplicacion es: ", multiplicacion)
print("La divicion es: ", divicion)
print("El resto de la divicion es: ", resto)   # saber el resto de un numero para saber si es divisible entre tal numero.

print("===============================")

# operadores aritmeticos ingresando 2 numeros por consola.

num1 = int(input("numero1: "))    #cuando querramos ingresar datos de tipo entero.
num2 = int(input("numero2: "))

print(f"La suma es: {num1+num2}")
print(f"la resta es: {num1-num2}")
print(f"la multiplicacion es: {num1*num2}")
print(f"la divicion es: {num1/num2}")
print(f"la reciduo es: {num1%num2}")

"""
¿Qué significa la F en un print de Python?
Una cadena "f" contiene variables y expresiones entre 
llaves "{}" que se sustituyen directamente por su valor. Las cadenas "f" 
se reconocen porque comienzan por una letra f antes de las comillas de apertura.

print(f"Me llamo {nombre} y tengo {edad} años. ")  

este formato indica que en la cadena a imprimir tiene variables de diferente tipo de datos.
"""