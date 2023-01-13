'''
Golf scores record the number of strokes used to get the ball in the hole. The expected number of strokes varies from hole to hole and is called par (i.e. 3, 4, or 5). Each score's name is based on the actual strokes taken compared to par:

    "Eagle": number of strokes is two less than par
    "Birdie": number of strokes is one less than par
    "Par": number of strokes equals par
    "Bogey": number of strokes is one more than par

Given two integers that represent par and the number of strokes used,
write a program that prints the appropriate score name. Print "Error" if par is not 3, 4, or 5.

'''

import math



par = int(input())
no_of_strokes = int(input())
outcome = no_of_strokes - par

if (par == 3) or (par == 4) or (par == 5):
    if (no_of_strokes < par) and (math.fabs(outcome) == 2):
        print('Eagle')
    elif (no_of_strokes < par) and (math.fabs(outcome) == 1):
        print('Birdie')
    elif (no_of_strokes == par):
        print('Par')
    elif (no_of_strokes > par) and (math.fabs(outcome) == 1):
        print('Bogey')
    else:
        print('Error')

else:
    print('Error')
   
