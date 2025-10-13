# Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
# siguiente situación:
# a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión.
import heap

monticulo = heap.HeapMax()

#a
monticulo.arrive("Sam", 1)
monticulo.arrive("Dean", 1)
monticulo.arrive("Castiel", 1)

#b
print("Primer elemento de la cola")
print(monticulo.attention()) #Imprime el primer elemento de la cola "Sam"

#c
monticulo.arrive("Bobby", 2)
monticulo.arrive("Crowley", 2)

#d
monticulo.arrive("Jack", 3)

#e
print("Dos primeros elementos de la cola")
print(monticulo.attention()) #Imprime el primer elemento de la cola "Dean"
print(monticulo.attention()) #Imprime el siguiente elemento de la cola "Castiel"

#f
monticulo.arrive("Roweena", 1)
monticulo.arrive("Charlie", 1)
monticulo.arrive("Lucifer", 3)

#g
print("Todos los elementos restantes de la cola") 
while monticulo.size() > 0: # Imprime todos los elementos restantes de la cola
    print(monticulo.attention())