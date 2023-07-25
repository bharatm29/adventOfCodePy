data = open("./input.txt").read().split('\n')
dictOfItems = {}

counter = 1
str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for c in str:
    dictOfItems[c] = counter
    counter += 1

ans = 0

for line in data:
    size = len(line)
    half = int(size / 2)

    st = set()

    for i in range(half):
        for j in range(half, size):
            if line[i] == line[j]:
                st.add(line[i])
    
    for item in st:
        ans += dictOfItems[item]

print(ans)