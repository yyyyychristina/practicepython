'''Figure 8.7.2: Modifying a list during iteration example: Converting negative values to 0. Incorrect way to modify the list.'''

user_input = input('Enter numbers:')

tokens = user_input.split()

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()
for pos, val in enumerate(nums):  
    
    print(f'{pos}: {val}')

# Change negative values to 0
for num in nums:
    if num < 0:
        num = 0  # Logic error: temp variable num set to 0

# Print new numbers
print('New numbers: ')
for num in nums:
    print(num, end=' ')
