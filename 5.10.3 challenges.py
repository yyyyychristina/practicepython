user_score = 0
simon_pattern = input()
user_pattern  = input()

for i in range(0,10):
    if simon_pattern[i] == user_pattern[i]:
        user_score += 1
    else:
        break
            
print('User score:', user_score)
