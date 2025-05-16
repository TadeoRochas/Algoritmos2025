
stack_trajes = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Dañado"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Impecable"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"},
    {"modelo": "Mark XL", "pelicula": "Iron Man 3", "estado": "Destruido"},
    {"modelo": "XLVII" , "pelicula": "Spiderman: Homecoming", "estado": "Dañado"},
    {"modelo": "Mark XLVI", "pelicula": "Captain America: Civil War", "estado": "Impecable"},
    ]

trajes_destruidos = []

#Punto a
#Sirve para buscar si el traje Mark XLIV aparece en alguna película y muestra el nombre de la pelicula donde sale.
def buscar_traje(stack_trajes, modelo):
    peliculas = []
    for traje in stack_trajes:
        if traje["modelo"] == "Mark XLIV":
            peliculas.append(traje["pelicula"])
    if peliculas:
        for pelicula in peliculas:
            print(f"El traje {modelo} aparece en la película {pelicula}.")
    else:
        print(f"El traje {modelo} no aparece en ninguna película.")

#Punto b
#Sirve para mostrar el nombre de los trajes Dañados.
def mostrarDañados(stack_trajes):
    for traje in stack_trajes:
        if traje["estado"] == "Dañado":
            print(f"El traje {traje['modelo']} de la película {traje['pelicula']} está dañado.")

#Punto c
#Sirve para eliminar los trajes con estado Destruido y tambien mostrar el nombre del mismo.
#Actualmente el código (no se por qué) solo toma uno de los dos trajes destruidos y no ambos.
def eliminarDestruidos(stack_trajes):
    trajesDestruidos = []
    for traje in stack_trajes:
        if traje["estado"] == "Destruido":
            trajesDestruidos.append(traje["modelo"])
            stack_trajes.remove(traje)
    return print(f"Los trajes destruidos fueron: {trajesDestruidos}")

def mostrarTrajes(stack_trajes):
    trajes_pelis = []
    for traje in stack_trajes:
        if traje["pelicula"] == "Spiderman: Homecoming" or traje["pelicula"] == "Capitan America: Civil War":
             trajes_pelis.append(traje["modelo"])
    return trajes_pelis
            
def agregarTraje(stack_trajes, modelo, pelicula, estado):
    nuevo_traje = {"modelo": modelo, "pelicula": pelicula, "estado": estado}
    stack_trajes.append(nuevo_traje)
    return stack_trajes

print(buscar_traje(stack_trajes, "Mark XLIV"))
print(mostrarDañados(stack_trajes))
print(eliminarDestruidos(stack_trajes))
print(stack_trajes)
print(agregarTraje(stack_trajes, "Mark LXXXVI", "Avengers: Endgame", "Impecable"))
print(mostrarTrajes(stack_trajes))
