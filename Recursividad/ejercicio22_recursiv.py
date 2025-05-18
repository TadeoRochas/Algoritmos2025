mochila_luck = ["comida", "abrigo", "sable de luz"]

def usar_la_fuerza(mochila_luck,contador=0):
    if not mochila_luck:
        return False, contador
    objeto = mochila_luck[0]
    if objeto == "sable de luz":
        contador += 1
        return True, contador
    else:
        resultado, contador = usar_la_fuerza(mochila_luck[1:], contador)
        if resultado:
            return True, contador
        else:
            return False, contador
        
    
lista = ["comida", "abrigo", "sable de luz"]

resultado, contador = usar_la_fuerza(lista)
if resultado:
    print(f"El sable de luz fue encontrado en la mochila y se ha usado {contador} veces.") 
else:   
    print("El sable de luz no fue encontrado en la mochila.")