data = open('input.txt', 'r').read().split('\n')

ans = 0
buffer = 0

for i in data:
    if i != '':
        buffer += int(i)
    else:
        ans = max(ans, buffer)
        buffer = 0

print(ans)