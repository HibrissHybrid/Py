"""
# Condicionales IF

estructura condicional if para la toma de deciiones si o no.

SI se_cumple_esta_condicion:
   Ejecutar grupo de instruciones.
SI NO:
   Se ejecutan otro grupo de instruciones.


if condicion:
    instruciones.
else:
    otras instruciones.


# Operadores de comparacion:

== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que


# Operadores Logicos:

and  Y
or  O
!  NEGACION
not  NO

"""

# Ejemplo 1

print("\n################# Ejemplo 1 #######################")

# color = "rosa"
color = input("cual es mi color favorito? ")

if color == "rosa":
   print("adivinaste")
else:
    print("no adivinaste xc ")


# Ejemplo 2

print("\n################## Ejemplo 2 ######################")

# year = 2020
year = int(input("en que ano estamos? "))

if year < 2021:
    print("estamos de 2021 en adelante")
else:
    print("es un ano posterior a 2021 ")



# Ejemplo 3

print("\n################## Ejemplo 3 ######################")

"""
 If Anidados 
 programa que imprima si eres mayor de edad y de que continente y ciudad eres.

 se ejecuta el primer IF y si se cumple, ejecuta el sig. IF
"""

nombre = "Hibran Hybrid"
ciudad = "Sinaloa"
continente = "Americano"   
edad = 24
mayor = 18


if edad >= mayor:
    print(f"{nombre} Es mayor de edad !!")

    if continente != "Americano":
       print("El usuario NO es Americano")
    else:
       print(f"ES Americano y de {ciudad}")
    
else:
    print(f"{nombre} NO es Mayor de edad. ")



# Ejemplo 4

print("\n################## Ejemplo 4 ######################")

#programa que te diga que dia de la semana es introduciendo su numero.


#dia = int(input("introduce el dia de la semana: "))

dia = 2
"""
if dia == 1:
    print("LUNES")
else:
    if dia == 2:
       print("MARTES")
    else:
        if dia == 3:
           print("MIERCOLES") 
        else:
            if dia == 4:
                print("JUEVES")
            else:
                if dia == 5:
                   print("MARTES")
                else:
                   print("WEEKEND")   
"""


if dia == 1:
    print("LUNES")
elif dia == 2:
    print("MARTES")
elif dia == 3:
    print("MIERCOLES")
elif dia == 4:
    print("JUEVES")
elif dia == 5:
    print("VIERNES")
else:
    print("WEEKEND")

# "elif" sino: tall instrucion.


# Ejemplo 5

print("\n################## Ejemplo 5 ######################")

"""
 Programa que indique si estas en condicion para trabajar

"""

edadmin = 18
edadmax = 65
# edadof = int(input("cual es tu edad? "))
edadof = 24
"""
Operador Logico "and" (" y ") 
if condicion and talcondicion
   se ejecuta tal instrucion
else
    otras instruciones 
"""     

if edadof >= 18 and edadof <= 65:
    print("Estas en edad para trabajar !!")
else:
    print("NO estas en ead de trabajar., ")


# Ejemplo 6

print("\n################## Ejemplo 6 ######################")

pais = "Mexico"

if pais == "Mexico" or pais == "Espana" or pais == "Colombia":
    print(f"{pais}, es un pais latinoamericano")
else:
    print(f"{pais}, no es un pais de habla hispana.")

# Si cumple 1ra  O 2da  O 3ra:

# Ejemplo 7

print("\n################## Ejemplo 7 ######################")


pais = "Mexico"

"""
 SI NO "es tales condiciones 1,2,3"
       ejecuta_instruciones
"""

if not (pais == "Mexico" or pais == "Espana" or pais == "Colombia"):
    print(f"{pais}, NO es un pais de habla hispana uwu")
else:
    print(f"{pais}, SI es un pais de habla hispana. !! ")

# Ejemplo 8

print("\n################## Ejemplo 8 ######################")

pais = "Mexico"
"""
si pais es DIFERENTE de "Mexico" Y pais DIF de "Espana" Y pais dIF de "Colombia"
    ejecuta_instruciones
"""

if pais != "Mexico" and pais != "Espana" and pais != "Colombia":
    print(f"{pais}, NO es un pais de habla hispana uwu")
else:
    print(f"{pais}, SI es un pais de habla hispana. !! ")



