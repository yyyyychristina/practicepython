'''
Exercise 2: Print the following pattern

Write a program to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''



no_row = int(input())


for i in range(1, no_row+1, 1):              #1, 2, 3, 4, 5
    for j in range(1, i+1):                        #(1,2), (1,3), (1,4), (1,5), (1,6)
        print(j, end=' ')

    print("")                                            #empty line after each row                           
 
