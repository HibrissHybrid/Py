"""
Diccionarios.
"tipo de datos"
tipo nde dato que almacena un conjunto de datos
en formato clave > valor.
es parecido a un array asociativo o un objeto json.

"""

persona = {
    "nombre": "hibran",
    "apellido": "larreta",
    "web": "udemy.com"
}

print(persona["nombre"])  # hibran   "de esta forma buscamos valor con su clave."


# diccionarios:

contactos = [
    {
        "nombre": "hibrancito",
        "email": "hibris@gmail.com"
    },
    {
        "nombre": "liz",
        "email": "liz@gmail.com"
    },
    {
        "nombre": "elkakas",
        "email": "kakas@gmail.com"
    }
]

contactos[0]['nombre'] = "hibran"   # aqui modificamos el nombre del primer contacto[0]['nombre']
print(contactos[0]['nombre']) # imprime el nuevo nombre

print("\nlistado de3 contactos: ")  # lista de cointactos

for contacto in contactos:  #contacto en contactos estoes para recorrer los elementos en la lista.
    print("\n")  # salto de linia
    print("---------------------------------------------")
    print(f"nombre del contacto: {contacto['nombre']}")  # imprime nombre y email.
    print(f"email del contacto: {contacto['email']}")
    print("---------------------------------------------")
