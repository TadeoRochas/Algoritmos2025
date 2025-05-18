#Dada una secuencia de caracteres, obtener dicha secuencia invertida.

def inverter(secuencia):
 if secuencia == "":
    return secuencia
 else:
    return inverter(secuencia[1:]) + secuencia[0]

sec = "hola profe"
sec_invertida = inverter(sec)
print (sec_invertida) # odnum aloh