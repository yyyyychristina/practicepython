'''Exercise 18: Print the following pattern

Write a program to print the following start pattern using the for loop

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
output = ''
output2 = '****'
for i in range(9):
    output = output + '*'
    if i >= 5:
        break
    print(output)
for i in range(6, 10):
    print(output2)
    output2 = '*' * (9-i)
    
