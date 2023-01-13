'''
Write a program in Python to display the Factorial of a number.

Hint 1 
Input : 5

Expected output 
Factorial is 120

Hint 1 
Input : 6
'''

user_input = int(input())
factorial = 1

for i in range(user_input, 0, -1):
    factorial *= i
print(factorial)
    
