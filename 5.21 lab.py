'''
Exercise 2: Write a program in Python to reverse a word.
'''

word = input()

for character in reversed(word):
    print(character, end='')
