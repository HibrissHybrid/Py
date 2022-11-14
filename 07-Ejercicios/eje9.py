"""
 Ejercicio 9. hacer un programa que pida numeros
  al usuario hasta ingresar la contrasena correcta "1111"

"""

count = 1
while count < 100:
    numero = int(input("introduce un Numero: "))

    if numero == 123:
        print("contrasena correcta! ")
        break
    else:
        print(f"error escribiste mal {numero}")
        print("Vuelve a intentarlo.")
