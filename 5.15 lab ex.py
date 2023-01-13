word = input()
password = ''

'''
Many user-created passwords are simple and easy to guess. 
Write a program that takes a simple password and makes it stronger by replacing characters using the key below, 
and by appending "!" to the end of the input string.

    i becomes 1
    a becomes @
    m becomes M
    B becomes 8
    s becomes $
'''

word = input()
password = ''

'''
Many user-created passwords are simple and easy to guess. 
Write a program that takes a simple password and makes it stronger by replacing characters using the key below, 
and by appending "!" to the end of the input string.

    i becomes 1
    a becomes @
    m becomes M
    B becomes 8
    s becomes $
'''

for i in word:
    if i == 'i':
        password += '1'
    
    elif i == 'a':
        password += '@'
    
    elif i == 'm':
        password += 'M'
        
    elif i == 'B':
        password += '8'
        
    elif i == 's':
        password += '$'
    
    else:
        password += i
        
        

    
print(f'{password}!')
