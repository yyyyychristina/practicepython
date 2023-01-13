'''
Exercise 10: Use else block to display a message “Done” after successful execution of for loop

For example, the following loop will execute without any error.

Given:

for i in range(5):
    print(i)

Expected output:

0
1
2
3
4
Done!
'''
my_dict_shopping = {'milk': 2, 'tuna': 4, 'cheese': 2, 'beef': 5, 'carrot': 1, 'tomato': 3, 'eggplant':2}

    
for j in my_dict_shopping:
    print(my_dict_shopping[j])

    
else:
    print('Done')
