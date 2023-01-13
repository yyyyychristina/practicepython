is_leap_year = False
   
input_year = int(input())

test_input_year = input_year % 4

century_year_input_year = input_year % 100

test2_input_year = input_year % 400

if test_input_year == 0:                      #filter out leap year that is divisible by 4
    if century_year_input_year == 0:    # filter out century number that is divisible by 400
        if test2_input_year == 0:            # filter out century number and leap year that is divisible by 4 and 400
            print(f'{input_year} - leap year')
        else:
            print(f'{input_year} - not a leap year')
        
    else:
        print(f'{input_year} - leap year')


else:
    print(f'{input_year} - not a leap year')
