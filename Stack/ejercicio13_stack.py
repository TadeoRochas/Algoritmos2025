from stack import Stack

class Traje:
    def __init__(self, modelo:str, pelicula:str, estado:str):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado
    def __str__(self):
        return f"Modelo: {self.modelo}, Película: {self.pelicula}, Estado: {self.estado}"

pila_trajes = Stack()

#punto d, los trajes fueron cargados manualmente a la pila respetando la consigna.
pila_trajes.push(Traje("Mark XLIV", "Avengers: Age of Ultron", "Dañado"))
pila_trajes.push(Traje("Mark L", "Avengers: Infinity War", "Destruido"))
pila_trajes.push(Traje("Mark LXXXV", "Avengers: Endgame", "Dañado"))
pila_trajes.push(Traje("Mark XLVI", "Capitan America: Civil War", "Impecable"))
pila_trajes.push(Traje("Mark XLVII", "Spider-Man: Homecoming", "Dañado"))
pila_trajes.push(Traje("Mark XLVIII", "Avengers: Infinity War", "Dañado"))
pila_trajes.push(Traje("Mark LXXX", "Avengers: Endgame", "Dañado"))
pila_trajes.push(Traje("Mark XLIX", "Avengers: Age of Ultron", "Destruido"))

#Punto a
#Esta funcion sirve para comprobar si el traje Mark XLIV forma parte de la pila, y retorna un mensaje en caso verdadero mostrando 
#el nombre de la pelicula. Para trabajar con la pila, hace una copia y trabaja sobre esa para no modificar la original.
def buscarTraje(buscado):
    copiaPila = pila_trajes.copy()
    pelicula = []
    while copiaPila.size() > 0:
        trajeActual = copiaPila.pop()
        if trajeActual.modelo == buscado:
            pelicula.append(trajeActual.pelicula)
    
    if pelicula:
        print(f"El traje {buscado} aparece en la película: {pelicula}")
    else:
        print("No se encontró el traje Mark XLIV en la pila.")

#Punto b
#Esta funcion sirve para almacenar en otra pila los nombres de los trajes dañados 
def trajesDañados():
    trajes_dañados = []
    copiaPila = pila_trajes.copy() #apunte: .copy() sirve para crear una copia de la pila original sin modificar la misma.

    while copiaPila.size() > 0:
        traje_actual = copiaPila.pop()
        if traje_actual.estado == "Dañado":
            trajes_dañados.append(traje_actual.modelo)

    if trajes_dañados:
        print(f"Los trajes dañados son: {trajes_dañados}")
    else:
        print("No hay trajes dañados en la pila.")

#Punto c
#Esta funcion sirve para extraer uno a uno los trajes de la pila original y almacenarlos en otra pila, pero solo si su estado 
#es distinto a "Destruido". Tambien los elimina de la pila orginal.
def eliminarDestruidos():
    trajesDestruidos = []
    trajesNoDestruidos = []
    
    while pila_trajes.size() > 0:
        trajeActual = pila_trajes.pop()
        if trajeActual.estado == "Destruido":
            trajesDestruidos.append(trajeActual)
        else:
            trajesNoDestruidos.append(trajeActual)
    
    if trajesDestruidos:
        print(f"Los trajes destruidos son: {[traje.modelo for traje in trajesDestruidos]}")

    while trajesNoDestruidos:
        pila_trajes.push(trajesNoDestruidos.pop())

#Punto e 
#Esta funcion sirve para agregar un traje a la pila, antes comprobando si existe en la misma.
def agregarTraje(modelo, pelicula, estado):
    copiaPila = pila_trajes.copy() 
    while copiaPila.size() > 0:
        trajeActual = copiaPila.pop()
        if (trajeActual.modelo == modelo) and (trajeActual.pelicula == pelicula):
            print(f"El traje {trajeActual.modelo} que sale en la pelicula {trajeActual.pelicula} ya existe en la pila.")
            return #apunte: return corta la funcion y no sucede lo siguiente.
        
    nuevo_traje = Traje(modelo, pelicula, estado)
    pila_trajes.push(nuevo_traje)
    print(f"El traje {modelo} ha sido agregado a la pila.")

#Esta funcion sirve para mostrar los trajes que hay en la pila.
def mostrarTrajes():
    if pila_trajes: #apunte: comprueba que la pila contiene elementos.
        print("Trajes actuales en la pila:")
        copiaPila = pila_trajes.copy()
        while copiaPila.size() > 0:
            trajeActual = copiaPila.pop()
            print(trajeActual)
    else:
        print("No hay trajes en la pila.")

#Esta funcion busca los trajes usados en dos peliculas especificas y los muestra.
def trajesUsados(buscado1,buscado2):
    trajes_usados = []
    copiaPila = pila_trajes.copy()
    while copiaPila.size() > 0:
        trajeActual = copiaPila.pop()
        if trajeActual.pelicula == buscado1 or trajeActual.pelicula == buscado2:	
            trajes_usados.append(trajeActual.modelo) 
            
    if trajes_usados: #Nota: a mi parecer se podría hacer un poco mas estético para que muestre en que peli se usó cada traje respectivamente, pero así igual está bien.
        print(f"Los trajes usados en las peliculas {buscado1} y {buscado2} son: {trajes_usados}")

#Llamado de las funciones

#Muestra la pila original de trajes:
mostrarTrajes()
print("--------------------------------------------------")
#llamado al punto a
buscarTraje("Mark XLIV")
print("--------------------------------------------------")
#llamado al punto b
trajesDañados() 
print("--------------------------------------------------")
#llamado al punto c
eliminarDestruidos()
print("--------------------------------------------------")
#llamado al punto e
agregarTraje("Mark LXXXV", "Avengers: Endgame", "Dañado")
print("--------------------------------------------------")
#llamado al punto f
trajesUsados("Spider-Man: Homecoming","Capitan America: Civil War")
print("--------------------------------------------------")

mostrarTrajes()



