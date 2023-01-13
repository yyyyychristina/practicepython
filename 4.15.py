num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 < num2:
    num2 = num1
    if num2 > num3:
        num2 = num3
        print(num2)
    else:
        print(num2)
else:
    num1 = num2
    if num1 > num3:
        num1 = num3
        print(num1)
    else:
        num3 = num1
        print(num3)
    
