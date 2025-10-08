# n. muestre las criaturas capturadas por Heracles.

from BinaryTree import BinaryTree

DATA = [
    {"criatura": "Ceto", "derrotado_por": "-", "descripcion": "Monstruo marino primordial"},
    {"criatura": "Tifón", "derrotado_por": "Zeus", "descripcion": "Gigante alado más poderoso"},
    {"criatura": "Equidna", "derrotado_por": "Argos Panoptes", "descripcion": "Madre de los monstruos"},
    {"criatura": "Dino", "derrotado_por": "-", "descripcion": "Una de las Greas"},
    {"criatura": "Pefredo", "derrotado_por": "-", "descripcion": "Una de las Greas"},
    {"criatura": "Enio", "derrotado_por": "-", "descripcion": "Una de las Greas"},
    {"criatura": "Escila", "derrotado_por": "-", "descripcion": "Monstruo marino con múltiples cabezas"},
    {"criatura": "Caribdis", "derrotado_por": "-", "descripcion": "Monstruo marino que crea remolinos"},
    {"criatura": "Euríale", "derrotado_por": "-", "descripcion": "Una de las Gorgonas"},
    {"criatura": "Esteno", "derrotado_por": "-", "descripcion": "Una de las Gorgonas"},
    {"criatura": "Medusa", "derrotado_por": "Perseo", "descripcion": "Gorgona con cabello de serpientes"},
    {"criatura": "Ladón", "derrotado_por": "Heracles", "descripcion": "Dragón de cien cabezas guardián"},
    {"criatura": "Águila del Cáucaso", "derrotado_por": "-", "descripcion": "Ave que torturaba a Prometeo"},
    {"criatura": "Quimera", "derrotado_por": "Belerofonte", "descripcion": "Híbrido de león, cabra y serpiente"},
    {"criatura": "Hidra de Lerna", "derrotado_por": "Heracles", "descripcion": "Serpiente de múltiples cabezas regenerativas"},
    {"criatura": "León de Nemea", "derrotado_por": "Heracles", "descripcion": "León con piel impenetrable"},
    {"criatura": "Esfinge", "derrotado_por": "Edipo", "descripcion": "Criatura con enigmas mortales"},
    {"criatura": "Dragón de la Cólquida", "derrotado_por": "-", "descripcion": "Guardián del vellocino de oro"},
    {"criatura": "Cerbero", "derrotado_por": "-", "descripcion": "Perro de tres cabezas guardián del inframundo"},
    {"criatura": "Cerda de Cromión", "derrotado_por": "Teseo", "descripcion": "Jabalí hembra gigante"},
    {"criatura": "Ortro", "derrotado_por": "Heracles", "descripcion": "Perro de dos cabezas"},
    {"criatura": "Toro de Creta", "derrotado_por": "Teseo", "descripcion": "Toro salvaje que escupía fuego"},
    {"criatura": "Jabalí de Calidón", "derrotado_por": "Atalanta", "descripcion": "Jabalí gigante enviado por Artemisa"},
    {"criatura": "Carcinos", "derrotado_por": "-", "descripcion": "Cangrejo gigante"},
    {"criatura": "Gerión", "derrotado_por": "Heracles", "descripcion": "Gigante de tres cuerpos"},
    {"criatura": "Cloto", "derrotado_por": "-", "descripcion": "Una de las Moiras, hila el hilo de la vida"},
    {"criatura": "Láquesis", "derrotado_por": "-", "descripcion": "Una de las Moiras, mide el hilo"},
    {"criatura": "Átropos", "derrotado_por": "-", "descripcion": "Una de las Moiras, corta el hilo"},
    {"criatura": "Minotauro de Creta", "derrotado_por": "Teseo", "descripcion": "Híbrido de hombre y toro"},
    {"criatura": "Harpías", "derrotado_por": "-", "descripcion": "Criaturas aladas con rostro de mujer"},
    {"criatura": "Argos Panoptes", "derrotado_por": "Hermes", "descripcion": "Gigante de cien ojos"},
    {"criatura": "Aves del Estínfalo", "derrotado_por": "-", "descripcion": "Aves con plumas de bronce"},
    {"criatura": "Talos", "derrotado_por": "Medea", "descripcion": "Autómata gigante de bronce"},
    {"criatura": "Sirenas", "derrotado_por": "-", "descripcion": "Criaturas que atraen con su canto"},
    {"criatura": "Pitón", "derrotado_por": "Apolo", "descripcion": "Serpiente gigante de Delfos"},
    {"criatura": "Cierva de Cerinea", "derrotado_por": "-", "descripcion": "Cierva con cuernos de oro"},
    {"criatura": "Basilisco", "derrotado_por": "-", "descripcion": "Serpiente que mata con la mirada"},
    {"criatura": "Jabalí de Erimanto", "derrotado_por": "-", "descripcion": "Jabalí gigante de Erimanto"},
]


arbol_criaturas = BinaryTree()

for criatura in DATA:
    arbol_criaturas.insert(
        criatura['criatura'], #se inserta el nombre de la criatura como value
        {
            "derrotado_por": criatura['derrotado_por'],
            "descripcion": criatura['descripcion'],
            #G agrego el campo "capturada" para saber si fue capturada o no.
            "capturada": "-"
        } #se inserta un diccionario con la perona que lo derrotó y la descripcion de la criatura. Este es el campo de other_values
    )

print()
print("-------------------------")
print()


#Agrego esta funcion para ver el arbol mas ordenado, se puede usar perfectamente el in_order que hicimos en clase.
def mostrar_arbol_limpio(arbol):
    def __mostrar(root):
        if root is not None:
            __mostrar(root.left)
            print(f"Criatura: {root.value}")
            print(f"  Derrotado por: {root.other_values['derrotado_por']}")
            print(f"  Capturada por: {root.other_values['capturada']}")
            print(f"  Descripción: {root.other_values['descripcion']}")
            print()
            __mostrar(root.right)
    
    __mostrar(arbol.root)


#A
print("Listado inorden de las criaturas y quienes la derrotaron:")
mostrar_arbol_limpio(arbol_criaturas)
#arbol_criaturas.in_order() #Se puede usar este metodo tambien, pero no es tan claro como el otro.
print()
print("-------------------------")
print()

#B
#Descripcion en el DATA

# print()
# print("-------------------------")
# print()

#C
print("Informacion de la criatura Talos:")
info = arbol_criaturas.search("Talos") #asigna a info el nodo que contiene a Talos
if info:
    print(f"Criatura: {info.value}"),
    print(f"Derrotado por: {info.other_values['derrotado_por']}"),
    print(f"Descripción: {info.other_values['descripcion']}")
else:
    print("No se encontro la criatura buscada")

print()
print("-------------------------") 
print()

#D

ranking_result = {} # Diccionario para almacenar el ranking de héroes
arbol_criaturas.ranking(ranking_result)

def ordenar_ranking(item):
    return item[1]

list_ranking = list(ranking_result.items())
list_ranking.sort(key=ordenar_ranking, reverse=True) #Ordeno la lista de mayor a menor segun la cantidad de criaturas derrotadas

print("Top 3 héroes que derrotaron más criaturas:")
print(list_ranking[:3]) #Muestro los 3 primeros elementos de la lista ordenada

print()
print("-------------------------") 
print()

#E
def listar_derrotadas_por(arbol, heroe):
    resultado = []
    def __listar_derrotadas_por(root, heroe):
        if root is not None:
            __listar_derrotadas_por(root.left, heroe)
            if root.other_values['derrotado_por'] == heroe: #comprueba que el heroe que derrotó a la criatura y el parametro sean iguales.
                resultado.append(root.value)
            __listar_derrotadas_por(root.right, heroe)

    __listar_derrotadas_por(arbol.root, heroe)
    return resultado

criaturas_derrotadas_por_heracles = listar_derrotadas_por(arbol_criaturas, "Heracles")
print("Criaturas derrotadas por Heracles:")
for criatura in criaturas_derrotadas_por_heracles:
    print(f" - {criatura}")

print()
print("-------------------------")  
print()

#F
def criaturas_no_derrotadas(arbol):
    resultado = []
    def __criaturas_no_derrotadas(root):
        if root is not None:
            __criaturas_no_derrotadas(root.left)
            if root.other_values['derrotado_por'] == "-": #si la criatura no ha sido derrotada, se agrega a la lista.
                resultado.append(root.value)
            __criaturas_no_derrotadas(root.right)
    __criaturas_no_derrotadas(arbol.root)
    return resultado

lista_criaturas_no_derrotadas = criaturas_no_derrotadas(arbol_criaturas)
print("Criaturas que no han sido derrotadas:")
for criatura in lista_criaturas_no_derrotadas:
    print(f" - {criatura}")

print()
print("-------------------------")  
print()

#G
#Ver linea 62.

#H
criaturas_capturadas = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"] #Lista de criaturas a modificar
print("Modificando criaturas capturadas por Heracles:")
for criatura in criaturas_capturadas:
    nodo = arbol_criaturas.search(criatura)
    if nodo:
        nodo.other_values["capturada"] = "Heracles"
        print(f" - {criatura} ahora está marcada como capturada por Heracles")
    else:
        print(f" - No se encontró la criatura: {criatura}")

print("-------------------------") 

#N 
def listar_capturadas_por(arbol, heroe):
    resultado = []
    def __listar_capturadas_por(root, heroe):
        if root is not None:
            __listar_capturadas_por(root.left, heroe)
            if root.other_values['capturada'] == heroe: #comprueba que el heroe que capturó a la criatura y el parametro sean iguales.
                resultado.append(root.value)
            __listar_capturadas_por(root.right, heroe)

    __listar_capturadas_por(arbol.root, heroe)
    return resultado


criaturas_capturadas_por_heracles = listar_capturadas_por(arbol_criaturas, "Heracles")
print("Criaturas capturadas por Heracles:")
for criatura in criaturas_capturadas_por_heracles:
    print(f" - {criatura}")


print()
print("-------------------------")  
print()

#I
def buscar_por_coincidencia(arbol, texto):
    resultado = []
    def __buscar_por_coincidencia(root, texto):
        if root is not None:
            __buscar_por_coincidencia(root.left, texto)
            if texto.lower() in root.value.lower(): #busca coincidencias sin importar mayusculas o minusculas
                resultado.append(root.value)
            __buscar_por_coincidencia(root.right, texto)

    __buscar_por_coincidencia(arbol.root, texto)
    return resultado

palabra_a_buscar = "de" #se puede cambiar esta palabra para buscar otras coincidencias
criaturas_encontradas = buscar_por_coincidencia(arbol_criaturas, palabra_a_buscar)
if criaturas_encontradas:
    print(f"Criaturas que contienen '{palabra_a_buscar}':")
    for criatura in criaturas_encontradas:
        print(f" - {criatura}")
else:
    print(f"No se encontraron criaturas que contengan '{palabra_a_buscar}'")

print()
print("-------------------------")  
print()

#J
print("Eliminando Basilisco y Sirenas del árbol:")
arbol_criaturas.delete("Basilisco")
arbol_criaturas.delete("Sirenas")
print("-------------------------")  
print("Basilisco y Sirenas han sido eliminados.")
basi = arbol_criaturas.search("Basilisco")
sire = arbol_criaturas.search("Sirenas")

print("-------------------------")  

if not basi and not sire:
    print("Verificación: Basilisco y Sirenas no se encuentran en el árbol.")

print()
print("-------------------------")  
print()

#K
nodo_aves_estinfalo = arbol_criaturas.search("Aves del Estínfalo")
if nodo_aves_estinfalo:
    nodo_aves_estinfalo.other_values['derrotado_por'] = "Heracles (varias veces)"
    print("Se ha modificado el nodo de las Aves del Estínfalo para indicar que Heracles las derrotó varias veces.")
    

print()
print("-------------------------")  
print()

#L
nodo_ladon = arbol_criaturas.search("Ladón")
if nodo_ladon:
    nodo_ladon.value = "Dragón Ladón"
    print("Se ha modificado el nombre de Ladón a Dragón Ladón.")

print()
print("-------------------------")
print()

#M
print("Listado por nivel del árbol:")
arbol_criaturas.by_level()

print()
print("-------------------------")
print()

print("Árbol completo después de todas las modificaciones:")
mostrar_arbol_limpio(arbol_criaturas)