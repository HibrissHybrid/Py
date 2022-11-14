"""
Ejercicio 5.
crear una lista con el contenidoi de la sig. tabla.:
accion      aventura        deportes
GTA         ASSIINS          FIFA21
COD           CRASH            PRO 21
PUBG         PRINCE            MOTO GP 21

Mostrar esta informacion ordenada:
"""

table = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "CALL OF DUTY", "PUBG"]
    },
    {
        "categoria": "AVENTURE",
        "juegos": ["ASSIINS", "CRASH", "PRINCE"]
    },
    {
        "categoria": "SPORT",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]


"""
creamos una tabla con la sig. sublista de videjuegos

y un for para poder recorrerla e imprimirla por pantalla.
"""

for categoria in table:
    print(f"-----------------{categoria['categoria']}---------------------")
    for juego in categoria['juegos']:   # me recorre la lista de juegos de cada categoria.
        print(juego)  # me imprime los juegos de cada categoria.