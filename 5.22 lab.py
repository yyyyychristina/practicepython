'''
Exercise 3: Write a Python program to reverse a number.

Hint 1 
Input a number to reverse : 43521

Expected output 
Result: 12534

# Reverse a number
'''

number = input()
output = ''

for i in range(len(number)-1, -1, -1):           # eg number = 369      # for i in range((3-1), -1, -1)   #output = '' + '9'  #output = '9' + '2' #output = '9''2' + '3'
    output = output + number[i]

print(output)
