'''
Exercise 6: Write a program that appends the square of each number to a new list.

Hint 1 
Given x = [2,3,4,5,6,7,8]



Expected output 
Result: [4, 9, 16, 25, 36, 49, 64]
'''
import math


my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
result = []




for i in range(len(my_list)):
    result.append(int(math.pow(my_list[i], 2)))

print(result)
    
