'''
Exercise 8: Write a program that appends the type of elements from a list.

Hint 1 
Given x = [23, ‘Python’, 23.98]

Expected output 
Result:
[<class ‘int’>,<class ‘str’>,<class ‘float’>

'''

my_list = [23, 'Python', 23.98]          #create a list
Result = []                                     #create an empty list



for j in my_list:
    Result.append(type(j))

print(Result)
