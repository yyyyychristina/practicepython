'''
Exercise 10: Write a program to fetch only even values from a dictionary.

Hint 1 
dic = {‘val1’:10, ‘val2’:20, ‘val3’:23, ‘val4’:22 }

Expected output 
Result : 10 20 22
'''

my_dict = {'val1': 10, 'val2': 20, 'val3': 23, 'val4': 22}




for i in my_dict:
    if my_dict[i] % 2 == 0:
        print(my_dict[i], end=' ')
        
        




    

