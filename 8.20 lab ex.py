'''
8.20 LAB: Car wash

Write a program to calculate the total price for car wash services.
A base car wash is $10. A dictionary with each additional service and the corresponding cost has been provided.
Two additional services can be selected. A '-' signifies an additional service was not selected.
Output all selected services, according to the input order, along with the corresponding costs and then the total price for all car wash services.

Ex: If the input is:

Tire shine
Wax

the output is:

ZyCar Wash
Base car wash -- $10
Tire shine -- $2
Wax -- $3
----
Total price: $15

Ex: If the input is:

Rain repellent
-

the output is:

ZyCar Wash
Base car wash -- $10
Rain repellent -- $2
----
Total price: $12
'''
services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()

if (service_choice1 != '-') and (service_choice2 != '-'):
    print('ZyCar Wash')
    print('Base car wash -- $10')
    print(f'{service_choice1} -- ${services.get(service_choice1, "N/A")}')
    print(f'{service_choice2} -- ${services.get(service_choice2, "N/A")}')
    print('----')
    total = 10 + (services.get(service_choice1, "N/A")) + (services.get(service_choice2, "N/A"))
    print(f'Total price: ${total}')

elif (service_choice1 != '-') and (service_choice2 == '-'):
    print('ZyCar Wash')
    print('Base car wash -- $10')
    print(f'{service_choice1} -- ${services.get(service_choice1, "N/A")}')
    print('----')
    total = 10 + (services.get(service_choice1, "N/A"))
    print(f'Total price: ${total}')
    
else:
    print('ZyCar Wash')
    print('Base car wash -- $10')
    print('----')
    total = 10
    print(f'Total price: ${total}')
    

