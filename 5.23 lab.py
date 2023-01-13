'''
Exercise 4: Write a program to print n natural number in descending order using a while loop.

Hint 1 
Enter a range : 10

Expected output 
Result: 10  9  8  7  6  5  4  3  2  1
'''

enter_a_range = int(input())
n = enter_a_range




while enter_a_range > 0:             # eg: 10 > 0
    while n > 0:                             #  10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1   x0
        print(n, end =' ')
        n = n - 1


    
