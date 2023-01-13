'''
Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.
If the input is:

Hello there
Hey
done

then the output is:

ereht olleH
yeH
'''

user_input = input()

while user_input != 'Done' and user_input != 'done' and user_input != 'd':
    output = ''
    for i in range(len(user_input)-1,-1,-1):
        output = output + user_input[i]
    print(output)
    user_input = input()




