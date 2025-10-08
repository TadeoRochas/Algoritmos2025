from BinaryTree import BinaryTree
from super_heroes_data_ import superheroes

# Primero se crea el arbol con los atributos del nombre y si es villano o no.
#A
arbol = BinaryTree()
for hero in superheroes:
    arbol.insert(hero['name'], hero['is_villain'])

#B
def villain_in_order():
    def __villain_in_order(root):
        if root is not None:
            __villain_in_order(root.left)
            if root.other_values is True:
                print(root.value)
            __villain_in_order(root.right)

    if arbol.root is not None:
        __villain_in_order(arbol.root)

#C
def superhero_starts_with(value):
    def __superhero_starts_with(root):
        if root is not None:
            __superhero_starts_with(root.left)
            if root.value.startswith(value):
                print(root.value)
            __superhero_starts_with(root.right)

    if arbol.root is not None:
        __superhero_starts_with(arbol.root)

#D
def count_superheroes(arbol):
    def __count_superheroes(root):
        if root is None:
            return 0
        left_count = __count_superheroes(root.left)
        right_count = __count_superheroes(root.right)
        return left_count + right_count + (1 if not root.other_values else 0) #Si other_values es False (es un superhéroe) le suma 1 al contador. Basicamente cuenta los nodos del arbol que no son villanos.

    if arbol.root is not None:
        return __count_superheroes(arbol.root)
    return 0

#E
#Ver código mas abajo

#F
def superheroes_descending():
    def __superheroes_descending(root): #Barrido en postorden.
        if root is not None:
            __superheroes_descending(root.right)  # Primero derecha (orden descendente)
            if not root.other_values:  # Imprime solo si es superhéroe
                print(root.value)
            __superheroes_descending(root.left)  # Después izquierda

    if arbol.root is not None:
        __superheroes_descending(arbol.root)


def count_villains(arbol):
    def __count_villains(root):
        if root is None:
            return 0
        left_count = __count_villains(root.left)
        right_count = __count_villains(root.right)
        return left_count + right_count + (1 if root.other_values else 0) #Si other_values es True (es un villano) le suma 1 al contador. Basicamente cuenta los nodos del arbol que son villanos.

    if arbol.root is not None:
        return __count_villains(arbol.root)
    return 0

print()
print("-------------------------")
print()

#B
print("Villanos ordenados alfabéticamente:")
villain_in_order()

print()
print("-------------------------")
print()

#C
print("Superheroes que empiezan por la letra C:")
superhero_starts_with("C")

print()
print("-------------------------")
print()

#D
print ("Cantidad de Superheroes en el arbol:")
print(count_superheroes(arbol))

print()
print("-------------------------")
print()

#E
print("Listado de superhéroes que comienzan con 'Dr':")
arbol.proximity_search("Dr")
arbol.delete("Dr Strange")
print("-------------------------")

print("Listado por proximidad luego del cambio:")
arbol.insert("Doctor Strange", False)
arbol.proximity_search("Dr")
print("-------------------------")

print("Verificacion de que el cambio fue exitoso:")
resultado = arbol.search("Doctor Strange")
if resultado:
    print(f"Encontrado: {resultado.value}, es villano: {resultado.other_values}")
else:
    print("No encontrado")

print()
print("-------------------------")
print()

#F
print("Superhéroes ordenados de manera descendente:")
superheroes_descending()

print()
print("-------------------------")
print()

#G
arbol_heroes = BinaryTree()
arbol_villains = BinaryTree()
arbol.divide_tree(arbol_heroes, arbol_villains)

print("Cantidad de superhéroes en el árbol de héroes:")
print(count_superheroes(arbol_heroes))
print("Cantidad de villanos en el árbol de villanos:")
print(count_villains(arbol_villains))

print("-------------------------")

print("Barrido ordenado alfabéticamente del árbol de héroes:")
arbol_heroes.in_order()
print("-------------------------")
print("Barrido ordenado alfabéticamente del árbol de villanos:")
arbol_villains.in_order()

print()
print("-------------------------")
print()

