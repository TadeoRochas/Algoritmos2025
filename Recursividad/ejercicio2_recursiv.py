def suma(num):
    if num == 0:
        return num
    else:
        return num + suma(num-1)

print(suma(5))