'''
Exercise 9: Write a program to filter even and odd number from a list.

Hint 1 
Given x = [10, 23, 24, 35, 65, 78, 90]

Expected output 
Even numbers: [10, 24, 78, 90] Odd numbers: [23, 35, 65]
'''

my_list = [10, 23, 24, 35, 65, 78, 90]
Even_numbers = []
Odd_numbers = []


for j in my_list:
    if j % 2 == 0:
        Even_numbers.append(j)

    else:
        Odd_numbers.append(j)

print(f'Even numbers: {Even_numbers} Odd numbers: {Odd_numbers}')
        
