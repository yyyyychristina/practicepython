
Age = int(input())
Weight = int(input())
Heart_rate = int(input())
Time = int(input())

Calories = ((Age * 0.2757) + (Weight * 0.03295) + (Heart_rate * 1.0781) - 75.4991) * Time / 8.368 

print(f'Calories: {Calories:.2f} calories')


