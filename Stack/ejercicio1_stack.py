stack = [1,5,7,9,5,2,1]
stackdos = []

def ocurrencias(stack):
    contador={}
    for i in stack:
        if i in contador:
            contador[i] += 1
        else:
            contador[i] = 1
    return contador


  
print(ocurrencias(stack))
