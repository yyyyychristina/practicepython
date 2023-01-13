total_change_amount = int(input())

if total_change_amount >= 100:
    no_of_dollars = total_change_amount // 100
    total_change_amount = total_change_amount - (100 * no_of_dollars)
    if total_change_amount >= 25:
        no_of_quarters = total_change_amount // 25
        total_change_amount = total_change_amount - (25 * no_of_quarters)
        if total_change_amount >= 10:
            no_of_dimes = total_change_amount // 10
            total_change_amount = total_change_amount - (10 * no_of_dimes)
            if total_change_amount >= 5:
                no_of_nickels = total_change_amount // 5
                total_change_amount = total_change_amount - (5 * no_of_nickels)
                if total_change_amount >= 1:
                    no_of_pennies = total_change_amount // 1
                    total_change_amount = total_change_amount - (1 * no_of_pennies)
                    print(f'{no_of_dollars} Dollar\n{no_of_quarters} Quarter\n{no_of_dimes} Dime\n{no_of_nickels} Nickel\n{no_of_pennies} Penny')
                else:
                    print(f'{no_of_dollars} Dollar\n{no_of_quarters} Quarter\n{no_of_dimes} Dime\n{no_of_nickels} Nickel')
            elif total_change_amount >= 1:
                no_of_pennies = total_change_amount // 1
                total_change_amount = total_change_amount - (1 * no_of_pennies)
                print(f'{no_of_dollars} Dollar\n{no_of_quarters} Quarter\n{no_of_dimes} Dime\n{no_of_pennies} Penny')
            else:
                print(f'{no_of_dollars} Dollar\n{no_of_quarters} Quarter\n{no_of_dimes} Dime\n{no_of_pennies} Penny')

        elif total_change_amount >= 5:
            no_of_nickels = total_change_amount // 5
            total_change_amount = total_change_amount - (5 * no_of_nickels)
            if total_change_amount >= 1:
                no_of_pennies = total_change_amount // 1
                total_change_amount = total_change_amount - (1 * no_of_pennies)
                print(f'{no_of_dollars} Dollar\n{no_of_quarters} Quarters\n{no_of_nickels} Nickel\n{no_of_pennies} Penny')
            else:
                print(f'{no_of_dollars} Dollar\n{no_of_quarters} Quarter\n{no_of_nickels} Nickel')
            
        elif total_change_amount >= 1:
            no_of_pennies = total_change_amount // 1
            total_change_amount = total_change_amount - (1 * no_of_pennies)
            print(f'{no_of_dollars} Dollar\n{no_of_pennies} Pennies')
        else:
            print(f'{no_of_dollars} Dollars')
        
    elif total_change_amount >= 10:
        no_of_dimes = total_change_amount // 10
        total_change_amount = total_change_amount - (10 * no_of_dimes)
        print(f'{no_of_dollars}Dollar\n{no_of_dimes} Dimes')
    elif total_change_amount >= 5:
        no_of_nickels = total_change_amount // 5
        total_change_amount = total_change_amount - (5 * no_of_nickels)
        print(f'{no_of_dollars}Dollar\n{no_of_nickels} Nickels')
    elif total_change_amount >= 1:
        no_of_pennies = total_change_amount // 1
        total_change_amount = total_change_amount - (1 * no_of_pennies)
        print(f'{no_of_dollars} Dollar\n{no_of_pennies} Pennies')
    else:
            print(f'{no_of_dollars} Dollars')
   
elif total_change_amount >= 25:
    no_of_quarters = total_change_amount // 25
    total_change_amount = total_change_amount - (25 * no_of_quarters)
    if total_change_amount >= 10:
        no_of_dimes = total_change_amount // 10
        total_change_amount = total_change_amount - (10 * no_of_dimes)
        print(f'{no_of_quarters} Quarter\n{no_of_dimes} Dimes')
    elif total_change_amount >= 5:
        no_of_nickels = total_change_amount // 5
        total_change_amount = total_change_amount - (5 * no_of_nickels)
        print(f'{no_of_quarters} Quarter\n{no_of_nickels} Nickels')
    else:
        no_of_pennies = total_change_amount // 1
        total_change_amount = total_change_amount - (1 * no_of_pennies)
        print(f'{no_of_quarters} Quarter\n{no_of_pennies} Pennies')

elif total_change_amount >= 10:
    no_of_dimes = total_change_amount // 10
    total_change_amount = total_change_amount - (10 * no_of_dimes)
    if total_change_amount >= 5:
        no_of_nickels = total_change_amount // 5
        total_change_amount = total_change_amount - (5 * no_of_nickels)
        print(f'{no_of_dimes} Dimes\n{no_of_nickels} Nickels')
    else:
        no_of_pennies = total_change_amount // 1
        total_change_amount = total_change_amount - (1 * no_of_pennies)
        print(f'{no_of_dimes} Dimes\n{no_of_pennies} Pennies')


elif total_change_amount >= 5:
    no_of_nickels = total_change_amount // 5
    total_change_amount = total_change_amount - (5 * no_of_nickels)
    if total_change_amount >= 1:
        no_of_pennies = total_change_amount // 1
        total_change_amount = total_change_amount - (1 * no_of_pennies)
        print(f'{no_of_nickels} Nickels\n{no_of_pennies} Pennies')
    else:
        print('No change')

elif total_change_amount >= 1:
        no_of_pennies = total_change_amount // 1
        total_change_amount = total_change_amount - (1 * no_of_pennies)
        print(f'{no_of_pennies} Pennies')
    
else:
    print('No change')
    
        
    
        
