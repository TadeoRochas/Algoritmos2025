from list_ import List

class Jedi:
    def __init__(self, nombre, maestros, colores_sable, especie):
        self.nombre = nombre
        self.maestros = maestros
        self.colores_sable = colores_sable
        self.especie = especie
    
    #Aclaración sobre el __str__, al inicio lo plantee simplemente para que muestre el nombre del Jedi y su especie
    #pero para que quede un poco mas prolijo y entendible, con ayuda de copilot lo cambié para que muestre todos los datos para que se entienda mejor.
    def __str__(self):
        if self.maestros:
            maestros_str = ""
            for i, maestro in enumerate(self.maestros): #enumerate sirve para obtener el índice y el valor al mismo tiempo
                if i == 0:
                    maestros_str = maestro
                else:
                    maestros_str = maestros_str + ", " + maestro
        else:
            maestros_str = "Ninguno"
        
        colores_str = ""
        for i, color in enumerate(self.colores_sable):
            if i == 0:
                colores_str = color
            else:
                colores_str = colores_str + ", " + color
        
        return f"Jedi: {self.nombre}\n  Especie: {self.especie}\n  Maestros: {maestros_str}\n  Colores de sable: {colores_str}"

def criterion_name(jedi: Jedi):
    return jedi.nombre

def criterion_species(jedi: Jedi):
    return jedi.especie

Jedis = List()

Jedis.insert_value(Jedi("Luke Skywalker", ["Obi-Wan Kenobi", "Yoda"], ["verde", "azul"], "Humano"))
Jedis.insert_value(Jedi("Anakin Skywalker", ["Obi-Wan Kenobi"], ["azul"], "Humano"))
Jedis.insert_value(Jedi("Obi-Wan Kenobi", ["Qui-Gon Jinn"], ["azul"], "Humano"))
Jedis.insert_value(Jedi("Yoda", [], ["verde"], "Desconocida"))
Jedis.insert_value(Jedi("Mace Windu", [], ["violeta"], "Humano"))
Jedis.insert_value(Jedi("Ahsoka Tano", ["Anakin Skywalker"], ["verde", "azul"], "Togruta"))
Jedis.insert_value(Jedi("Rey", ["Luke Skywalker"], ["amarillo"], "Humano"))
Jedis.insert_value(Jedi("Qui-Gon Jinn", [], ["verde"], "Humano"))
Jedis.insert_value(Jedi("Kit Fisto", [], ["verde"], "Nautolano"))
Jedis.insert_value(Jedi("Aayla Secura", ["Quinlan Vos"], ["azul"], "Twi'lek"))
Jedis.insert_value(Jedi("Numa Rar", [], ["verde"], "Twi'lek"))
Jedis.insert_value(Jedi("Tott Doneeta", [], ["verde"], "Twi'lek"))


# A Ordenar la lista por nombre y especie
# Lista ordenada por nombre alfabeticamente
Jedis.add_criterion('name', criterion_name)
Jedis.sort_by_criterion('name')

print("Lista ordenada por nombre:")
Jedis.show()

print()
print("-------------------------")
print()

# Lista ordenada por especie
Jedis.add_criterion('species', criterion_species)
Jedis.sort_by_criterion('species')

print("Lista ordenada por especie:")
Jedis.show()

print()
print("-------------------------")
print()

#B Mostrar la informacion de Ahsoka Tano y Kit Fisto
index_ahsoka = Jedis.search("Ahsoka Tano", "name") #Controla que Ahsoka Tano esté en la lista
if index_ahsoka is not None:
    print("Información de Ahsoka Tano:")
    print(Jedis[index_ahsoka])

print()

index_kit_fisto = Jedis.search("Kit Fisto", "name") #Controla que Kit Fisto esté en la lista
if index_kit_fisto is not None: 
    print("Información de Kit Fisto:") 
    print(Jedis[index_kit_fisto]) 

print()
print("-------------------------")
print()

#C Listar los aprendices de Yoda y Luke Skywalker
index_yoda = Jedis.search("Yoda", "name") #Controla que Yoda esté en la lista
if index_yoda is not None:
    print("Aprendices de Yoda:") 
    for jedi in Jedis:
        if "Yoda" in jedi.maestros: #Corrobora que Yoda esté en la lista de maestros de cada Jedi
            print(jedi)

print()

index_luke = Jedis.search("Luke Skywalker", "name") #Controla que Luke esté en la lista
if index_luke is not None: 
    print("Aprendices de Luke Skywalker:")
    for jedi in Jedis:
        if "Luke Skywalker" in jedi.maestros: #Corrobora que Luke Skywalker esté en la lista de maestros de cada Jedi
            print(jedi)

print()
print("-------------------------")
print()

#D Mostrar los jedi de especie Humano y Twi'lek
print("Jedi de especie Humano:")
for jedi in Jedis:
    if jedi.especie == "Humano": #Corrobora que la especie sea Humano
        print(jedi)

print()

print("Jedi de especie Twi'lek:")
for jedi in Jedis:
    if jedi.especie == "Twi'lek": #Corrobora que la especie sea Twi'lek 
        print(jedi)

print()
print("-------------------------")
print()

#E Listar todos los Jedi que comienzan con A
print("Jedi que comienzan con la letra A:")
for jedi in Jedis:
    if jedi.nombre.startswith('A'): #Corrobora que el nombre comience con la letra A
        print(jedi)

print()
print("-------------------------")
print()

#F Mostrar los Jedi que usaron sable de luz de más de un color
print("Jedi que usaron sable de luz de más de un color:")
for jedi in Jedis:
    if len(jedi.colores_sable) > 1: #Corrobora que el tamaño del campo colores_sable sea mayor que 1
        print(jedi)

print()
print("-------------------------")
print()

#G Indicar los Jedi que usaron sable de luz amarillo o violeta.
print("Jedi que usaron sable de luz amarillo o violeta:")
condicion = False #Variable para controlar si se encontró algún Jedi que cumpla la condición.
for jedi in Jedis:
    if ("amarillo" in jedi.colores_sable or "violeta" in jedi.colores_sable): #Corrobora que el campo colores_sable contenga amarillo o púrpura.
        print(jedi)
        condicion = True #Cambia el valor de la variable si se encuentra algún Jedi que cumpla la condición

if not condicion: #Si no se encontró ningún Jedi que cumpla la condición, muestra un mensaje.
    print(" - No hay Jedi que usaron sable de luz amarillo o violeta.")


print()
print("-------------------------")
print()

#H Indicar los nombres de los aprendices de Qui-Gon Jinn y Mace Windu
print("Nombres de los aprendices de Qui-Gon Jinn:")
condicion_qui_gon = False #Variable para controlar si se encontró algún aprendiz de Qui-Gon Jinn.
for jedi in Jedis:
    if "Qui-Gon Jinn" in jedi.maestros:
        print(jedi.nombre)
        condicion_qui_gon = True #Cambia el valor de la variable si se encuentra algún aprendiz de Qui-Gon Jinn.

if not condicion_qui_gon: #Si no se encontró ningún aprendiz de Qui-Gon Jinn, muestra un mensaje.
    print(" - No hay aprendices de Qui-Gon Jinn.")

print()

print("Aprendices de Mace Windu:")
condicion_mace_windu = False #Variable para controlar si se encontró algún aprendiz de Mace Windu.
for jedi in Jedis:
    if "Mace Windu" in jedi.maestros:
        print(jedi.nombre)
        condicion_mace_windu = True #Cambia el valor de la variable si se encuentra algún aprendiz de Mace Windu.

if not condicion_mace_windu: #Si no se encontró ningún aprendiz de Mace Windu, muestra un mensaje.
    print(" - No hay aprendices de Mace Windu.")
