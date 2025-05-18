

stack = [1,5,7,9,5,2,1]
stackdos = []

def invertir(stack):
    for i in stack:
        stackdos = stack[::-1]
    return stackdos

print(stack)
print(invertir(stack))