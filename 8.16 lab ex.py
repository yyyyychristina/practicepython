'''
8.16 LAB: Varied amount of input data

Statistics are often calculated with varying amounts of input data. Write a program that takes any number of integers as input, and outputs the average and max.

Ex: If the input is:

15 20 0 5

the output is:

10 20

Note: For output, round the average to the nearest integer.
'''

user_input = input()
tokens = user_input.split()

new_tokens = [int(i) for i in tokens]    #make strings in the list called tokens into integar


print(int(sum([i for i in new_tokens]) / len(new_tokens)), end=' ')
#print out the average by adding all items in the list new_tokens
# and divided by its length
print(max(new_tokens))
#print out the maximum by the built-in function
