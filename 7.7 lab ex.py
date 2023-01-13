'''
7.7 LAB: Count characters

Write a program whose input is a string which contains a character and a phrase,
and whose output indicates the number of times the character appears in the phrase.
The output should include the input character and use the plural form, n's, if the number of times the characters appears is not exactly 1.

Ex: If the input is:

n Monday

the output is:

1 n

Ex: If the input is:

z Today is Monday

the output is:

0 z's

Ex: If the input is:

n It's a sunny day

the output is:

2 n's

Case matters. n is different than N.

Ex: If the input is:
n Nobody

the output is:

0 n's
'''
users_input = input()
tokens = users_input.split()      #separate the letter for counting and the word

count = 0                                                 # set count = 0 to let the for loop counts
for i in range(1, len(tokens)):         # make a loop to count all words
    count += tokens[i].count(tokens[0])

if count == 1:                                        
    print(f'{count} {tokens[0]}')

else:
    print(f'{count} {tokens[0]}\'s')



