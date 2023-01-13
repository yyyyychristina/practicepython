'''
8.17 LAB: Filter and sort a list

Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).

Ex: If the input is:

10 -7 4 39 -6 12 2

the output is:

2 4 10 12 39 

For coding simplicity, follow every output value by a space. Do not end with newline.
'''

user_input = input()
tokens = user_input.split()   #make input into a list
new_tokens = [int(i) for i in tokens]    #make strings in a list into integers


non_negative = []
for i in range(len(new_tokens)):        #for loop to filter out negative integar
    if new_tokens[i] >= 0:
        non_negative.append(new_tokens[i])   #add non_negative integars into the empty list



non_negative.sort()                              #make non_negative integars into acending order


for i in range(len(non_negative)):
    print(non_negative[i], end=' ')
