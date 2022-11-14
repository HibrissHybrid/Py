"""

# FOR

 for  variable in elemento_interable (lista,tulpa, rango, etc)
     BLOQUE DE INSTRUCCIONES
"""

contador = 0
resultado = 0

for contador in range(1,11):
    print("voy a contar.." + str(contador))

    resultado += contador

print(f"El resultado es: {resultado}")


# Ejemplo de tablas de multiplicar 
print("\n######### EJEMPLO #########")

numerou = int(input("de que numero quieres la tabla de muiltiplicar? "))

if numerou < 1:
    numerou = 1

print(f"\n###### Tabla de multiplicar del numero {numerou} ########")



for numerot in range(1,11):   #numerot en un rango DEL 1 al 11  

    if numerou == 45:    # ejemplo para romper el bucle "45 es un numero prohibido"
        print("No se puieden mostrar numeros prohibidos") 
        break  # este break rompe el bucle y hace que se salga del programa.

    print(f"{numerou} x {numerot} = {numerou*numerot}")  # aqui se hace la multiplicacion.
else: 
    print("Tabla Finalizada")

