# 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios para resolver las tareas, listadas a continuación:

# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servi- dor, router, switch, impresora;
# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch;
# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora;
# d. encontrar el árbol de expansión mínima;
# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
# f. indicar desde que computadora del switch 1 es el camino más corto al servidor “MongoDB”;
# g. cambiar la conexión de la impresora al router 2 y vuelva a resolver el punto b;
# h. debe utilizar un grafo no dirigido.

from graph_ import Graph

# Crear el grafo
grafo = Graph(is_directed=False)

# a) Nodos con nombre y tipo de dispositivo

# Notebooks
grafo.insert_vertex('Red Hat', 'notebook')
grafo.insert_vertex('Debian', 'notebook')
grafo.insert_vertex('Arch', 'notebook')

# PCs
grafo.insert_vertex('Manjaro', 'pc')
grafo.insert_vertex('Ubuntu', 'pc')
grafo.insert_vertex('Mint', 'pc')
grafo.insert_vertex('Parrot', 'pc')
grafo.insert_vertex('Fedora', 'pc')

# Servidores
grafo.insert_vertex('Guaraní', 'servidor')
grafo.insert_vertex('MongoDB', 'servidor')
# Routers
grafo.insert_vertex('Router 1', 'router')
grafo.insert_vertex('Router 2', 'router')
grafo.insert_vertex('Router 3', 'router')
# Switches
grafo.insert_vertex('Switch 1', 'switch')
grafo.insert_vertex('Switch 2', 'switch')

# Impresora
grafo.insert_vertex('Impresora', 'impresora')

# Aristas entre nodos con sus pesos
grafo.insert_edge('Red Hat', 'Router 2', 25)
grafo.insert_edge('Debian', 'Switch 1', 17)
grafo.insert_edge('Ubuntu', 'Switch 1', 18)
grafo.insert_edge('Switch 1', 'Impresora', 22)
grafo.insert_edge('Switch 1', 'Mint', 80)
grafo.insert_edge('Switch 1', 'Router 1', 29)
grafo.insert_edge('Router 2', 'Guaraní', 9)
grafo.insert_edge('Router 2', 'Router 1', 37)
grafo.insert_edge('Router 1', 'Router 3', 43)
grafo.insert_edge('Router 2', 'Router 3', 50)
grafo.insert_edge('Manjaro', 'Switch 2', 40)
grafo.insert_edge('Router 3', 'Switch 2', 61)
grafo.insert_edge('Switch 2', 'Parrot', 12)
grafo.insert_edge('Switch 2', 'Fedora', 3)
grafo.insert_edge('Switch 2', 'Arch', 56)
grafo.insert_edge('Switch 2', 'MongoDB', 5)


# b) Barrido en profundidad y amplitud desde las notebooks Red Hat, Debian y Arch
notebooks = ['Red Hat', 'Debian', 'Arch']
for notebook in notebooks: 
    print(f'Barrido en profundidad desde {notebook}:')
    grafo.deep_sweep(notebook)
    print()
    print("-------------------------")
    print()
    print(f'Barrido en amplitud desde {notebook}:')
    grafo.amplitude_sweep(notebook)
    print()
    print("-------------------------")
    print()

# c) Camino más corto desde Manjaro, Red Hat, Fedora hasta la impresora
for pc in ['Manjaro', 'Red Hat', 'Fedora']:
    path = grafo.dijkstra(pc)  # Path contiene los nodos del grafo con información de costos y predecesores
    #Basicamente path tiene [nombre_nodo, costo_acumulado, nodo_previo]    

    # Reconstruir el camino hasta la impresora
    destination = 'Impresora'
    peso_total = None
    camino_completo = []
    
    while path.size() > 0:
        value = path.pop()
        # value = [nombre_nodo, costo_acumulado, nodo_previo]
        if value[0] == destination: # Comprueba si es el nodo destino
            if peso_total is None:
                peso_total = value[1] # Guarda el costo total al llegar a la impresora
            camino_completo.append(value[0]) # Agrega el nodo al camino
            destination = value[2]  # Retrocede al nodo anterior
    
    camino_completo.reverse()
    
    if camino_completo:
        print(f'Camino más corto desde {pc} hasta la Impresora:')
        print(f'  Ruta: {" -> ".join(camino_completo)}')
        print(f'  Costo total: {peso_total}')
    else:
        print(f'No hay camino desde {pc} hasta la Impresora')
    print("-------------------------\n")

# d) Árbol de expansión mínima
expansion_tree = grafo.kruskal('Red Hat') 
print(expansion_tree)

# Calcular peso total
peso_total = 0
for edge in expansion_tree.split(';'):
    origin, destination, weight = edge.split('-')
    print(f'{origin} → {destination}: {weight}')
    peso_total += int(weight)
print("-------------------")
print(f'Peso total del MST: {peso_total}')

print()
print("-------------------------")
print()

# e) Desde qué pc (no notebook) es el camino más corto hasta el servidor "Guaraní"
pcs = ['Manjaro', 'Ubuntu', 'Mint', 'Parrot', 'Fedora']
mejor_pc = None
menor_costo = float('inf')
mejor_camino = []

for pc in pcs:
    path = grafo.dijkstra(pc)
    
    # Reconstruir el camino hasta Guaraní
    destination = 'Guaraní'
    peso_total = None
    camino_completo = []
    
    while path.size() > 0:
        value = path.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]
    
    camino_completo.reverse()
    
    # Comparar si este es el camino más corto
    if peso_total is not None and peso_total < menor_costo:
        menor_costo = peso_total
        mejor_pc = pc
        mejor_camino = camino_completo

print(f'La PC con el camino más corto a Guaraní es: {mejor_pc}')
print(f'  Ruta: {" -> ".join(mejor_camino)}')
print(f'  Costo total: {menor_costo}')

print()
print("-------------------------")
print()

# f) indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;
computadoras_switch1 = ['Debian', 'Ubuntu', 'Mint']
mejor_computadora = None
menor_costo = float('inf')
mejor_camino = []
for computadora in computadoras_switch1:
    path = grafo.dijkstra(computadora)
    
    # Reconstruir el camino hasta MongoDB
    destination = 'MongoDB'
    peso_total = None
    camino_completo = []
    
    while path.size() > 0:
        value = path.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]
    
    camino_completo.reverse()
    
    # Comparar si este es el camino más corto
    if peso_total is not None and peso_total < menor_costo:
        menor_costo = peso_total
        mejor_computadora = computadora
        mejor_camino = camino_completo

print(f'La computadora del Switch 1 con el camino más corto a MongoDB es: {mejor_computadora}')
print(f'  Ruta: {" -> ".join(mejor_camino)}')
print(f'  Costo total: {menor_costo}')

print()
print("-------------------------")
print()

# g) Cambiar la conexión de la impresora al router 02 y volver a resolver el punto b;
# Eliminar la arista entre Switch 1 e Impresora (pasando 'value' como criterio)
resultado = grafo.delete_edge('Switch 1', 'Impresora', 'value')
if resultado:
    print("Arista Switch 1 - Impresora eliminada exitosamente")
else:
    print("No se pudo eliminar la arista")

# Agregar la nueva arista entre Router 2 e Impresora
grafo.insert_edge('Router 2', 'Impresora', 2)
print("Nueva arista Router 2 - Impresora agregada con peso 2\n")

# Volver a resolver el punto b
print("Resolviendo punto b con nueva configuración:\n")

notebooks = ['Red Hat', 'Debian', 'Arch']
for notebook in notebooks: 
    print(f'Barrido en profundidad desde {notebook}:')
    grafo.deep_sweep(notebook)
    print()
    print("-------------------------")
    print()
    print(f'Barrido en amplitud desde {notebook}:')
    grafo.amplitude_sweep(notebook)
    print()
    print("-------------------------")
    print()