def producto(num1:int,num2:int) -> int:
    if num1==0 or num2==0:
        return 0
    else:
        return num1 * num2


result = producto(2,3)
print(result)