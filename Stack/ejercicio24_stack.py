from stack import Stack

class Personaje:
    def __init__ (self, nombre:str, cantidad_peliculas:int):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas
    def __str__(self):
        return f"Nombre: {self.nombre}, Cantidad de películas: {self.cantidad_peliculas}"
    
pila_personajes = Stack()

pila_personajes.push(Personaje("Iron Man", 7))
pila_personajes.push(Personaje("Capitan America", 6))
pila_personajes.push(Personaje("Thor", 5))
pila_personajes.push(Personaje("Rocket Raccoon", 4))
pila_personajes.push(Personaje("Hulk", 4))
pila_personajes.push(Personaje("Black Widow", 5))
pila_personajes.push(Personaje("Hawkeye", 6))
pila_personajes.push(Personaje("Doctor Strange", 3))
pila_personajes.push(Personaje("Groot", 4))
pila_personajes.push(Personaje("Spider Man", 4))
pila_personajes.push(Personaje("Black Panther", 2))

#Muestra la pila de personajes
def mostrarPila():
    copiaPila = pila_personajes.copy()
    while copiaPila.size() > 0:
        personajeActual = copiaPila.pop()
        print(personajeActual)

#Punto a
#Muestra la posición de un personaje buscado
def posicionPersonaje(buscado):
    personaje_buscado = []
    posicion_buscado = []
    copiaPila = pila_personajes.copy()

    while copiaPila.size() > 0:
        personajeActual = copiaPila.pop()
        if personajeActual.nombre == buscado:
            personaje_buscado.append(personajeActual.nombre)
            posicion_buscado.append(copiaPila.size())

    if personaje_buscado:
        print(f"El personaje {buscado} se encuentra en la posición: {posicion_buscado}")
    else:
        print(f"El personaje {buscado} no se encuentra en la pila.")

#Punto b
#Muestra los personajes que aparecen en más de 5 películas y su cantidad de películas
def personajesConMasPeliculas():
    personajes = []
    copiaPila = pila_personajes.copy()
    while copiaPila.size() > 0:
        personajeActual = copiaPila.pop()
        if personajeActual.cantidad_peliculas > 5:
            personajes.append((personajeActual.nombre, personajeActual.cantidad_peliculas)) #apunte: se usa doble parenteis como una Tupla, la cual permite almacenar varios valores juntos.

    if personajes:
        for personaje, cantidad in personajes:
            print(f"Los personajes {personaje} aparecen en {cantidad} películas.")
    else:
        print("No hay personajes que aparezcan en 5 o más películas.")

#Punto c
#Muestra la cantidad de películas en las que aparece un personaje buscado
def cantPeliculasPersonajeBuscado(buscado):
    
    cantidad_peliculas = []
    copiaPila = pila_personajes.copy()
    while copiaPila.size() > 0:
        personajeActual = copiaPila.pop()
        if personajeActual.nombre == buscado:
            cantidad_peliculas.append(personajeActual.cantidad_peliculas)

    if cantidad_peliculas:
        print(f"El personaje {buscado} aparece en {cantidad_peliculas} películas.")
    else:
        print(f"El personaje {buscado} no se encuentra en la pila.")

#Punto d
#Muestra los personajes que comienzan con una letra buscada
def mostrarPersonajesConLetra(buscado):
    personajes = []
    copiaPila = pila_personajes.copy()
    while copiaPila.size() > 0:
        personajeActual = copiaPila.pop()
        if personajeActual.nombre.startswith(buscado): #apunte: .startswith() sirve para saber si una cadena empieza con una letra/palabra especifica.
            personajes.append(personajeActual.nombre)

    if personajes:
        print(f"Los personajes que comienzan con la letra {buscado} son: {personajes}")
    else:
        print(f"No hay personajes que comiencen con la letra {buscado}.")

#llamado a las funciones

mostrarPila()
print("-----------------------------------")
posicionPersonaje("Rocket Raccoon")
posicionPersonaje("Groot")
print("-----------------------------------")
personajesConMasPeliculas()
print("-----------------------------------")
cantPeliculasPersonajeBuscado("Black Widow")
print("-----------------------------------")
mostrarPersonajesConLetra("C")
mostrarPersonajesConLetra("D")
mostrarPersonajesConLetra("G")
print("-----------------------------------")