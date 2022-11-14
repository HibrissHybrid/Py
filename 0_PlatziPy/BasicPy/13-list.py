"""

Almacenar varios valores en una variable: list

"""

# Como crear listas:

my_list = []
my_list = list()

# Como unir listas

my_list = [1]
my_list2 = [2,3,4]
my_list3 = my_list + my_list2
my_list # [1,2,3,4]

# Partir listas como slices(pedazos)

my_list = [1,2,3]
my_list[1:] = [2,3]

# Extender una lista

my_list =[1]
my_list2 =[2,3,4]
my_list.extend(my_list2)  #[1,2,3,4]

# Multiplicar Listas

my_list = ['a']
my_list2 = my_list * 5
my_list2 # ['a''a''a''a''a']

# Eliminar el ultimo elemento de la lista

my_list = [1,2,3,4,5]
my_list = my_list.pop()
my_list # [1,2,3,4]  # se elimina el ultimo elemento de la listacon .pop()

# Ordenar una Lista

my_list = [2,1,5,4,3]
my_list = my_list.sort()
my_list # [1,2,3,4,5]

# Eliminar un Atributo
my_list = [1,2,3,4,5]
del my_list[0]  # elimina la primera posicion.
my_list # [2,3,4,5]

# Eliminar si conoccemos su valor

my_list = [1,2,3,4,5]
my_list = my_list.remove(3)    # conocemos que el 3 se eliminara de la lista.
my_list # [1,2,4,5]

# Saber que metodo hay dentro de un Elemento.

my_list = [1,2,3,4,5]
dir(my_list) # ['__add__', '__class__', '__contains__']

# Modificar un Elemento

my_list = [1,2,3,4,5]
my_list[0] = 100    # en la posicion 0 = 100(elemento)
my_list # [100,2,3,4,5]

# Anadir un Elemento al Final

my_list = [1,2,3,4,5]
my_list.append(6)   # metodo .append para agregar un elemento, en el ultimo lugar,
my_list # [1,2,3,4,5,6]    # se agrega un 6 a la lista.

# Organizar una Lista

my_list = [2,5,1,3,4]
my_list.sort() # [1,2,3,4,5]   # .sort organiza de menor a mayor una lista desordenada.

"""
.sorted()
También ordena como sort() pero modifica la lista inicial

.clear()
Vacía la lista


.count()
Cuenta las veces que esta un elemento en lista


.index()
Indica la posición donde esta un elemento de la lista


.insert()
Inserta un elemento en una posición dada ej: lista.insert(posición,item)


.reverse()
Le da la vuelta a una lista

"""

