from random import randint

stack = [randint(1, 100) for i in range(10)]
stackpares = []

def removeimpares(stack):
    for i in stack:
        if i % 2 == 0:
            stackpares.append(i)
    return stackpares

print (stack)
print (removeimpares(stack))