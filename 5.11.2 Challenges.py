stop = -10
total = 0
for number in [5, 4, 5, 2, 3, 5]:
    print(number, end=' ')
    total -= number
    if total <= stop:
        print('!')
        break
else:
    print(f'/ {total}')
print('done')
