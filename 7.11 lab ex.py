'''
7.11 LAB: Remove all non-alpha characters

Write a program that removes all non-alpha characters from the given input.

Ex: If the input is:

-Hello, 1 world$!

the output is:

Helloworld
'''

users_input = input()

tokens = users_input.split()     #split the input in the list called tokens

result = ''                              #make an empty string
for i in range(len(tokens)):                 # for each items in the list called tokens
    for j in range(len(tokens[i])):             #for each letters in one item
        if tokens[i][j].islower() or tokens[i][j].isupper():                      #if a letter in the item is (a-z) or (A-Z)
            result += tokens[i][j]
        
    

print(result)
