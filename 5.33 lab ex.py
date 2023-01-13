'''
Exercise 4: Write a program to print multiplication table of a given number

For example, num = 2 so the output should be

2
4
6
8
10
12
14
16
18
20
'''

num = int(input())
output = 0

while num > 0:
    while output < 20:
        output = output + num
        print(output)
