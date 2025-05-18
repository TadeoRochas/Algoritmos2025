def pot (num, exponente):
    if exponente == 0:
        return 1
    else:
        return num**exponente
    
result = pot(3,2)
print(result)