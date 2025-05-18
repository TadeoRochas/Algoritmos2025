def serie(n):
    if n == 1:
        return n
    else:
        return 1/n + serie(n-1)
    
n = int(input("Ingrese un numero entero y positivo: "))
res = serie(n)
print("El resultado es: ", res)