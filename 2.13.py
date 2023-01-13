gas_milage = float(input())
cost_of_gas = float(input())

gas_cost_20miles = cost_of_gas / gas_milage * 20
gas_cost_75miles = cost_of_gas / gas_milage * 75
gas_cost_500miles = cost_of_gas / gas_milage * 500

print(f'{gas_cost_20miles:.2f} {gas_cost_75miles:.2f} {gas_cost_500miles:.2f}')


