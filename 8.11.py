'''
 A list can be useful in solving various engineering problems.
 One problem is computing the voltage drop across a series of resistors.
 If the total voltage across the resistors is V, then the current through the resistors will be I = V/R, where R is the sum of the resistances.
 The voltage drop Vx across resistor x is then Vx = I · Rx.
'''
 
'''
zyDE 8.11.1: Calculate voltage drops across series of resistors.

The following program uses a list to store a user-entered set of resistance values and computes I.

Modify the program to compute the voltage drop across each resistor, store each in another list voltage_drop, and finally print the results in the following format: 
'''

num_resistors = 5
resistors = []
voltage_drop = []


print(f'{num_resistors} resistors are in the series.')
print('This program calculates the'),
print('voltage drop across each resistor.')

input_voltage = float(input('Input voltage applied to circuit: '))
print (input_voltage)


print(f'Input ohms of {num_resistors} resistors')
for i in range(num_resistors):
    
    res = float(input(f'{i + 1}) '))
    print(res)
    resistors.append(res)

#  Calculate current
current = input_voltage / sum(resistors)

# Calculate voltage drop over each resistor
print('Voltage drop per resistor is')
for i in range(len(resistors)):
    Vx = current * resistors[i]
    print(f'{i+1}) {Vx:.1f} V')      # Print the voltage drop per resistor

