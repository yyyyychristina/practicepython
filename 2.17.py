no_of_quarters = int(input())
no_of_dimes = int(input())
no_of_nickels = int(input())
no_of_pennies = int(input())

dollars = no_of_quarters * 0.25 + no_of_dimes * 0.10 + no_of_nickels * 0.05 + no_of_pennies * 0.01

print(f'Amount: ${dollars:.2f}')
