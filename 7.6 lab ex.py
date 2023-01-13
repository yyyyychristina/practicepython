name_input = input()

tokens = name_input.split()


tokens2 = ((tokens[0])[0])

tokens3 = ((tokens[1])[0])


if len(tokens) > 2:
    print(f'{tokens[-1]}, {tokens2}.{tokens3}.')
    
else:
    print(f'{tokens[-1]}, {tokens2}.')
    
