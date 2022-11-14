def palindromo(palabra):      # funcion palindromo con parametro palabra.
    palabra = palabra.replace(" ", "")  # quitar espacios 
    palabra = palabra.lower()  #convertir texto a minisculas
    palabra_invertida = palabra[::-1]  # creamos texto invertido
    if palabra == palabra_invertida:   # si texto invertido es igual al texto. 
        return True   # devuelve true.  verdadero si es un palindromo.
    else:
        return False  # si no lo es devuelve falso.

def run():   # crea funcion correr. para validar la palabra palindromo. 
    palabra = input("escribe una palabra:  ")   # escribir una palabra
    es_palindromo = palindromo(palabra)  # comparamos con  nuestra funcion palindromo(osea la logica para identificar a un palindromo.)
    if es_palindromo == True:   # si es verdo 
        print("es palindromo :)  ")  # imprimimos que es un palindromo
    else:
        print("no es palindromo chale :(  ")    # en dado contrario no lo es.

if __name__ == '__main__':
    run()