'''
8.3.3: Hourly temperature reporting.
Write a loop to print all elements in hourly_temperature. Separate elements with a -> surrounded by spaces.

Sample output for the given program with input: '90 92 94 95'

90 -> 92 -> 94 -> 95 

Note: 95 is followed by a space, then a newline.
'''
for temperature in hourly_temperature:      
    if temperature == hourly_temperature[-1]:    # omit the last temperature
        break
    print(temperature, end=' -> ')                     #give output
print(hourly_temperature[-1], end=' ')            # lastly, print the last temperature in order to remove '->'
print()


