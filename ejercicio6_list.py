from list_ import List
from super_heroes_data import superheroes
class Superhero:
    
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f"{self.name}, {self.real_name} - {self.is_villain}"

def order_by_name(item):
    return item.name

list_superhero = List()
list_superhero.add_criterion('name', order_by_name)


for superhero in superheroes:
    hero = Superhero(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    list_superhero.append(hero)

print("Lista original: ")
list_superhero.show()

print()
print("-------------------------")
print()

#A eliminar a Groot
print(list_superhero.delete_value('Groot', 'name'))
print("Lista con el personaje ya eliminado:")
list_superhero.show()

print()
print("-------------------------")
print()

#B mostrar el año de aparicion de Wolverine
index = list_superhero.search('Wolverine', 'name')
if index:
    print(f"El año de aparicion de Wolverine es: {list_superhero[index].first_appearance}")
else:
    print('el superheroe no esta ne la lista')

print()
print("-------------------------")
print()

#C modificar Dr strage de villano a heroe
index = list_superhero.search('Dr Strange', 'name')
if index:
    print(list_superhero[index].is_villain)
    list_superhero[index].is_villain = False
    print(list_superhero[index].is_villain)
    print("Dr. Strange es un heroe ahora.")
else:
    print('el superheroe no esta ne la lista')

print()
print("-------------------------")
print()

#Dmostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
print('Superheroes con traje:')
for superhero in list_superhero:
    if 'armor' in superhero.short_bio or 'suit' in superhero.short_bio:
        print(superhero)

print()
print("-------------------------")
print()

#E mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
print('Superheroes que aparecen antes de 1963')
for superhero in list_superhero:
    if superhero.first_appearance < 1963:
        print(superhero.name)

print()
print("-------------------------")
print()

#F mostrar el nombre real de Capitan America y Ant Man;
#Capitan America:
index = list_superhero.search('Captain America', 'name')
if index:
    print(f"El nombre real de Capitan America es: {list_superhero[index].real_name}")
else:
    print("El superheroe no aparece en la lista.")
#Ant Man
index = list_superhero.search('Ant Man', 'name')
if index:
    print(f"El nombre real de Ant Man es: {list_superhero[index].real_name}")
else:
    print("El superheroe no aparece en la lista.")

print()
print("-------------------------")
print()

#G mostrar toda la información de Scarlet Witch y Starfox;
#Scarlet Witch
index = list_superhero.search('Scarlet Witch', 'name')
if index:
    print(f"La informacion de Scarlet Witch es: {list_superhero[index]}")
else:
    print("El personaje no está en la lista.")

#Star Lord
index = list_superhero.search('Starfox', 'name')
if index:
    print(f"La informacion de Starfox es: {list_superhero[index]}")
else:
    print("El personaje no está en la lista.")

print()
print("-------------------------")
print()

#H listar los superhéroes que comienzan con la letra B, M y S;
print("Los superheroes que comienzan con las letras B, M y S son:")
for superhero in list_superhero:
    if superhero.name.startswith(('B', 'M', 'S')):
        print(superhero)

print()
print("-------------------------")
print()

#I La consigna original pide determinar cuantos superheroes hay en cada casa,
#pero como nuestra lista no tiene el atributo Casa, opto por listar la cantidad de Heroes y Villanos.
heroes_count = 0
villains_count = 0
for superhero in list_superhero:
    if superhero.is_villain:
        villains_count += 1
    else:
        heroes_count += 1

print(f"Cantidad de Heroes: {heroes_count}")
print(f"Cantidad de Villanos: {villains_count}")