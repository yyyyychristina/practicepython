stop = int(input())
result = 0
for n in range(10):
    result += n + 2
    if result > stop:
        break
    print(n)
print(result)
