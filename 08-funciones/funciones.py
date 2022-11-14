"""

FUNCIONES EN PYTHON

una funcion te permite definir un bloque de codigo reutilizable
que se puede ejecutar muchas veces dentro de tu programa.

Las funciones te permiten crear soluciones mas modulares y DRY para
problemas complejos.

Si bien Python ya proporciona muchas funciones integradas 
como print() , sum(), len(), tambien puede definir tus propios
funciones para usar en tu proyectos.

uno de las frandes ventajas de usar funciones en tu codigo es que 
reduce el numerio total de codigo en tu proyecto.

"""

# función sin parámetros o retorno de valores
def diHola():
  print("Hello!")

diHola()  # llamada a la función, 'Hello!' se muestra en la consola

# función con un parámetro
def holaConNombre(name):
  print("Hello " + name + "!")

holaConNombre("hibran hybrid.")  # llamada a la función, 'Hello Ada!' se muestra en la consola

# función con múltiples parámetros con una sentencia de retorno
def multiplica(val1, val2):
  return val1 * val2

multiplica(3, 5)  # muestra 15 en la consola



"""
Las funciones son bloques de código que se pueden reutilizar simplemente llamando a la función. Esto permite la reutilización de código simple y elegante sin volver a escribir explícitamente secciones de código. Esto hace que el código sea más legible, facilita la depuración y limita los errores de escritura.

Las funciones en Python se crean usando la palabra clave def, seguida de un nombre de función y parámetros de función entre paréntesis.

Una función siempre devuelve un valor. La función utiliza la palabra clave return  para devolver un valor; si no desea devolver ningún valor, se devolverá el valor predeterminado None.

El nombre de la función se usa para llamar a la función, pasando los parámetros necesarios entre paréntesis.
"""

# esta es una función básica de suma
def suma(a, b):
  return a + b

result = suma(1, 2)
# result = 3

"""
Puedes definir valores predeterminados para los parámetros,
de esa manera Python interpretará que el valor de ese parámetro es el predeterminado si no se proporciona ninguno.



def suma(a, b=3):
  return a + b

result = suma(1)
# result = 4
# Puedes pasar los parámetros en el orden que desees, utilizando el nombre del parámetro.

result = suma(b=2, a=2)
# result = 4
# Sin embargo, no es posible pasar un argumento de palabra clave antes que uno que no sea de palabra clave

result = suma(3, b=2)
#result = 5
result2 = suma(b=2, 3)
#Lanzará SyntaxError
# Las funciones también son objetos, por lo que puedes asignarlas a una variable y usar esa variable como una función.

s = suma
result = s(1, 2)
# result = 3


Notas
Si la definición de una función incluye parámetros, debe proporcionar el mismo número de parámetros cuando llame a la función.

print(multiplica(3))  # TypeError: multiplica() utiliza exactamente 2 argumentos (0 proporcionados)

print(multiplica('a', 5))  # 'aaaaa' mostrado en la consola

print(multiplica('a', 'b'))  # TypeError: Python no puede multiplicar dos strings
El bloque de código que ejecutará la función incluye todas las declaraciones con indentación dentro de la función.

def miFunción():
    print('this will print')
    print('so will this')

x = 7
# la asignación de x no es parte de la función ya que no está indentada
Las variables definidas dentro de una función solo existen dentro del ámbito de esa función.

def duplica(num):
    x = num * 2
    return x

print(x)  # error - x no está definida
print(duplica(4))  # muestra 8
"""