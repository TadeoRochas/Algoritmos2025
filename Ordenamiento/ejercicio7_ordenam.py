personajes_sw= ["Luke", "Leia", "Han Solo","Hera", "Darth Maul", "Yoda", "Darth Vader"]

def ordenamiento_personajes(personajes_sw):
    personajes_sw.sort()
    return personajes_sw

def buscado(personajes_sw, buscado):
    for personaje in personajes_sw:
        if personaje == buscado:
            print(f"El personaje {buscado} fue encontrado en la lista.")
    
def buscados_antes_despues_hera(personajes_sw):
        if "Hera" in personajes_sw:
            index = personajes_sw.index("Hera")
            antes = personajes_sw[:index]
            despues = personajes_sw[index+1:]
            print (f"Personajes que están antes de Hera: {antes}")
            print (f"Personajes que estan despues de Hera: {despues}")

def personajes_L(personajes_sw):
    personajes_con_L = [personaje for personaje in personajes_sw if personaje.startswith("L")]
    print(f"Personajes que empiezan con 'L': {personajes_con_L}")

print(ordenamiento_personajes(personajes_sw))
print(buscado(personajes_sw, "Darth Maul"))
print(buscados_antes_despues_hera(personajes_sw))
print(personajes_L(personajes_sw))