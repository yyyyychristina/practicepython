input_month = input()
input_day = int(input())

months= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if (input_month in months) and (input_day > 0) and (input_day <= 31):               #filter out invalid data like chips and 88
    if (input_month == 'March') and (input_day >= 20) and (input_day <= 31):       #condition for each months and days: Spring: March 20 - June 20
        print('Spring')
    elif (input_month == 'April') and (input_day <= 30):
        print('Spring')
    elif (input_month == 'May') and (input_day <= 31):
        print('Spring')
    elif (input_month == 'June') and (input_day <= 20):
        print('Spring')
    elif (input_month == 'June') and (input_day >= 21) and (input_day <= 30):      #condition for each months and days : Summer: June 21 - September 21
        print('Summer')
    elif (input_month == 'July') and (input_day <= 31):
        print('Summer')
    elif (input_month == 'August') and (input_day <= 31):
        print('Summer')
    elif (input_month == 'September') and (input_day <= 21):
        print('Summer')
    elif (input_month == 'September') and (input_day >= 22) and (input_day <= 30):  # condition for each months and days: Autumn: September 22 - December 20
        print('Autumn')
    elif (input_month == 'October') and (input_day <= 31):
        print('Autumn')
    elif (input_month == 'November') and (input_day <= 31):
        print('Autumn')
    elif (input_month == 'December') and (input_day <= 20):
        print('Autumn')
    elif (input_month == 'December') and (input_day >= 21) and (input_day <= 30): #condition for each months and days: Winter: December 21 - March 19
        print('Winter')
    elif (input_month == 'January') and (input_day <= 31):
        print('Winter')
    elif (input_month == 'February') and (input_day <= 28):
        print('Winter')
    elif (input_month == 'March') and (input_day <= 19):
        print('Winter')
    else:
        print('Invalid')
    
else:
    print('Invalid')
