# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.

from graph_ import Graph

grafo = Graph(is_directed=False)
# a) Nodos con nombre de ambientes
ambientes = ['cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2', 'habitación 1', 'habitación 2', 'sala de estar', 'terraza', 'patio']
for ambiente in ambientes:
    grafo.insert_vertex(ambiente)

# b) Aristas entre nodos con sus pesos (distancia en metros)
# cocina
grafo.insert_edge('cocina', 'comedor', 5)
grafo.insert_edge('cocina', 'patio', 10)
grafo.insert_edge('cocina', 'baño 1', 7)
grafo.insert_edge('cocina', 'habitación 1', 12)

# comedor
grafo.insert_edge('comedor', 'sala de estar', 8)
grafo.insert_edge('comedor', 'terraza', 12)
grafo.insert_edge('comedor', 'cochera', 12)
grafo.insert_edge('comedor', 'habitación 1', 6)
grafo.insert_edge('comedor', 'baño 2', 15)

# cochera
grafo.insert_edge('cochera', 'quincho', 15)
grafo.insert_edge('cochera', 'patio', 20)
grafo.insert_edge('cochera', 'terraza', 22)
grafo.insert_edge('cochera', 'sala de estar', 25)

# quincho
grafo.insert_edge('quincho', 'terraza', 6)
grafo.insert_edge('quincho', 'patio', 18)
grafo.insert_edge('quincho', 'baño 2', 14)
grafo.insert_edge('quincho', 'habitación 1', 20)

# baño 1
grafo.insert_edge('baño 1', 'habitación 1', 4)
grafo.insert_edge('baño 1', 'habitación 2', 9)
grafo.insert_edge('baño 1', 'sala de estar', 13)
grafo.insert_edge('baño 1', 'terraza', 11)

# baño 2
grafo.insert_edge('baño 2', 'habitación 2', 3)
grafo.insert_edge('baño 2', 'terraza', 16)
grafo.insert_edge('baño 2', 'habitación 1', 8)

# habitación 2
grafo.insert_edge('habitación 2', 'sala de estar', 10)
grafo.insert_edge('habitación 2', 'comedor', 14)
grafo.insert_edge('habitación 2', 'terraza', 7)

# sala de estar
grafo.insert_edge('sala de estar', 'terraza', 9)
grafo.insert_edge('sala de estar', 'patio', 13)

# c) árbol de expansión mínima
arbol_expansion = grafo.kruskal('cocina')
peso_total = 0

print("Árbol de expansión mínima:")
aristas = arbol_expansion.split(';')
for arista in aristas:
    if arista:  # Evitar strings vacíos
        origen, destino, peso = arista.split('-')
        peso_int = int(peso)
        peso_total += peso_int
        print(f"{origen} -- {destino} (Peso: {peso_int} metros)")

print(f"\nMetros de cable necesarios: {peso_total} metros")
print("-------------------------")

# d) determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.
camino = grafo.dijkstra('habitación 1')
destino = 'sala de estar'

peso_total = None
camino_completo = []

while camino.size() > 0:
    valor = camino.pop()
    if valor[0] == destino:
        if peso_total is None:
            peso_total = valor[1]
        camino_completo.append(valor[0])
        destino = valor[2]

camino_completo.reverse()

if camino_completo:
    print(f'Camino más corto desde habitación 1 hasta sala de estar:')
    print(f'  Ruta: {" -> ".join(camino_completo)}')
    print(f'  Costo total: {peso_total} metros')
    print(f"Se necesitan {peso_total} metros de cable de red para conectar el router con el Smart Tv.")
else: 
    print(f'No hay camino desde habitación 1 hasta sala de estar')
print("-------------------------\n")