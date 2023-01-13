'''
8.18 LAB: Elements in a range

Write a program that first gets a list of integers from input.
That list is followed by two more integers representing lower and upper bounds of a range.
Your program should output all integers from the list that are within that range
(inclusive of the bounds).

Ex: If the input is:

25 51 0 200 33
0 50

the output is:

25 0 33 

The bounds are 0-50, so 51 and 200 are out of range and thus not output.

For coding simplicity, follow each output integer by a space, even the last one.
Do not end with newline.
'''

user_input = input()        #input numbers 
tokens = user_input.split()           #split into strings and put into a list
new_tokens = [int(i) for i in tokens]    #make each string into integers





ranges = input()             #input ranges e.g. 0 50
tokens2 = ranges.split()               #split into strings and put into a list
new_tokens2 = [int(i) for i in tokens2]   #make each string into integers


for i in range(len(new_tokens)):
    if (new_tokens[i] >= new_tokens2[0]) and (new_tokens[i] <= new_tokens2[1]):
        print(new_tokens[i], end=' ')
