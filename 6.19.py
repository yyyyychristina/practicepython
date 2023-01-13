def driving_cost(miles_per_gallon = 20.0, dollars_per_gallon = 3.1599, miles_driven = 50.0):
    driving_cost = dollars_per_gallon / miles_per_gallon * miles_driven
    return driving_cost
    
    
if __name__ == '__main__':
    miles_per_gallon = float(input())# Type your code here.
    dollars_per_gallon = float(input())
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 50):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 400):.2f}')
