"""
# BUCLES WHILE
Estructuras de control que itera o repite la ejecutacion
de una serie de instrucciones tantas veces sea necesario, 
hasta cumplirse la condicion.

while condicion:
    bloque de instrucciones
    actualizacion de comntador

"""

# Programa que me cuente los numeros del 1 al 100

contador = 1

while contador <= 100:
    print(f"Estoy contando.. {contador}")
    contador += 1


print("-------------------------")

# Programa que me cuente los numeros del 1 al 100, separados por una coma(,) 

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1
print(muestrame)


# EJEMPLO

numerou = int(input("cual tabla de multiplicar quieres? "))

if numerou < 1:
    numerou = 1


print(f"###### Tabla de multiplicar de {numerou} #####")

contador = 1    # contador empieza en 1
while contador <= 10:   # mientras contador sea menor o igual a 10
    print(f"{numerou} X {contador} = {numerou*contador}")  # se hace la multip[licacion]
    contador += 1  # se incrementa el contador
else:
    print("Tabla terminada.")   # tabla terminada.


