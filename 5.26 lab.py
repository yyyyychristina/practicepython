'''
Exercise 7: WAP to separate positive and negative number from a list.

Hint 1 
Given x = [23, 4, -6, 23, -9, 21, 3, -45, -8]

Expected output 
Result:
Positive: [23, 4, 23, 21, 3] Negative: [-6, -45, -9, -8]
'''

my_list = [23, 4, -6, 23, -9, 21, 3, -45, -8]
Positive = []
Negative = []


for i in range(len(my_list)):
    if my_list[i] >= 0:
        Positive.append(my_list[i])

    else:
        Negative.append(my_list[i])

print(f'Positive: {Positive} Negative: {Negative}')
        
        
    
