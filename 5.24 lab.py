'''
Exercise 5: Write a program to display the first 7 multiples of 7.

Hint 1 
Use if and for loop with break

Expected output 
Result: 0  7  14  21  28  35  42  49
'''
n = 0
for i in range(8):                     #range: 0, 1, 2, 3, 4, 5, 6, 7
        n = i * 7                       # 0, 7, 14, 21, 28, 35, 42, 49
        print(n, end=' ')
    
