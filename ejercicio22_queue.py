from queue_ import Queue

class Superheroe:
    def __init__(self, nombre:str, superheroe:str, genero:str):
        self.nombre = nombre
        self.superheroe = superheroe
        self.genero = genero
    def __str__(self):
        return f"Nombre: {self.nombre}, Superhéroe: {self.superheroe}, Género: {self.genero}"

cola_superheroes = Queue()

cola_superheroes.arrive(Superheroe("Tony Stark", "Iron Man", "Masculino"))
cola_superheroes.arrive(Superheroe("Peter Parker", "Spider Man", "Masculino"))
cola_superheroes.arrive(Superheroe("Natasha Romanoff", "Black Widow", "Femenino"))
cola_superheroes.arrive(Superheroe("Wanda Maximoff", "Scarlet Witch", "Femenino"))
cola_superheroes.arrive(Superheroe("Steve Rogers", "Capitan America", "Masculino"))
cola_superheroes.arrive(Superheroe("Bruce Banner", "Hulk", "Masculino"))
cola_superheroes.arrive(Superheroe("Carol Danvers", "Capitana Marvel", "Femenino"))
cola_superheroes.arrive(Superheroe("Thor Odinson", "Thor", "Masculino"))
cola_superheroes.arrive(Superheroe("Stephen Strange", "Doctor Strange", "Masculino"))
cola_superheroes.arrive(Superheroe("Gamora", "Gamora", "Femenino"))
cola_superheroes.arrive(Superheroe("Scott Lang", "Ant Man" , "Masculino"))
cola_superheroes.arrive(Superheroe("Loki Laufeyson", "Loki", "Masculino"))
cola_superheroes.arrive(Superheroe("Peter Quill", "Star-Lord", "Masculino"))

#Punto a
#Esta funcion sirve para buscar un superheroe por su apodo y mostrar su nombre.
def mostrarNombreBuscado(buscado):
    colaAuxiliar = cola_superheroes.qCopy() #apute: Realiza una copia de la cola para no desorganizar la original
    for i in range(colaAuxiliar.size()):
        if colaAuxiliar.on_front().superheroe == buscado:
            print(f"El nombre del superheroe buscado es: {colaAuxiliar.on_front().nombre}")
            break
        else:
            colaAuxiliar.move_to_end()
    else:
        print("No se encontró el superhéroe.")

#Punto b y c
#Esta funcion sirve para mostrar los nombres de los superhéroes femeninos y masculinos segun lo que se le ingrese.
def MostrarNombreGenero(gen):
    colaAuxiliar = cola_superheroes.qCopy()
    personajesGenero = []
    for i in range(colaAuxiliar.size()):
        if colaAuxiliar.on_front().genero == gen:
            personajesGenero.append(colaAuxiliar.on_front().nombre)
        colaAuxiliar.move_to_end()
    
    if personajesGenero:
        print(f"Los superhéroes de género {gen} son:")
        for superheroe in personajesGenero:
            print(superheroe)

#Punto d
#Esta funcion sirve para buscar un superheroe por su nombre y mostrar su apodo.
def mostrarSuperheroeNombre(buscado):
    colaAuxiliar = cola_superheroes.qCopy()
    for i in range(colaAuxiliar.size()):
        if colaAuxiliar.on_front().nombre == buscado:
            print(f"El apodo del superhéroe buscado es: {colaAuxiliar.on_front().superheroe}")
            break #apunte: si el personaje se encuentra, imprime el apodo y termina el ciclo.
        colaAuxiliar.move_to_end()
    else:
        print("No se encontró el superhéroe.")

#Punto e
#Esta funcion sirve para mostrar los superhéroes o personajes que comienzan con una letra determinada.
#El ejercicio dice "superheroe o personaje", por lo que consideré ambos. 
#En caso de solo tener que mostrar superhéroes, se puede cambiar la condicion y eliminar del "or" en adelante.
def mostrarDatosLetra(letra):
    colaAuxiliar = cola_superheroes.qCopy()
    personajesLetra = []
    for i in range(colaAuxiliar.size()):
        if colaAuxiliar.on_front().nombre.startswith(letra) or colaAuxiliar.on_front().superheroe.startswith(letra):
            personajesLetra.append(colaAuxiliar.on_front())
        colaAuxiliar.move_to_end()
        
    if personajesLetra:
        print(f"Los superhéroes o heroes que comienzan con la letra {letra} son:")
        for superheroe in personajesLetra:
            print(superheroe)

#Punto f
#Esta funcion sirve para buscar un personaje por su nombre y mostrar su apodo.
def buscarPersonajeExiste(buscado):
    colaAuxiliar = cola_superheroes.qCopy()
    for i in range(colaAuxiliar.size()):
        if colaAuxiliar.on_front().nombre == buscado:
            print(f"El personaje {buscado} está en la cola y su apodo es {colaAuxiliar.on_front().superheroe}")
            break 
        colaAuxiliar.move_to_end()
    else:
        print(f"El personaje {buscado} no está en la cola.")


#Esta funcion sirve para mostrar todos los superhéroes que hay en la cola.
def mostrarCola():
    for i in range(cola_superheroes.size()):
        print(cola_superheroes.on_front())
        cola_superheroes.move_to_end()



print("Superhéroes en la cola:")
mostrarCola()
print("------------")
#Punto a
mostrarNombreBuscado("Capitana Marvel")
print("------------")
#Punto b
MostrarNombreGenero("Femenino")
print("------------")
#Punto c
MostrarNombreGenero("Masculino")
print("------------")
#Punto d
mostrarSuperheroeNombre("Scott Lang")
print("------------")
#Punto e
mostrarDatosLetra("S")
print("------------")
#Punto f
buscarPersonajeExiste("Carol Danvers")
print("------------")
print("Superhéroes en la cola después de buscar:")
mostrarCola()