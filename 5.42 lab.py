'''
Exercise 14: Reverse a given integer number

Given:

76542

Expected output:

24567
'''

number = input()

for i in reversed(number):
    print(i, end='')
