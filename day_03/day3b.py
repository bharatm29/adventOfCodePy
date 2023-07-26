data = open("./input.txt").read().split('\n')
dictOfItems = {}

counter = 1
str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for c in str:
    dictOfItems[c] = counter
    counter += 1

ans = 0
i = 0

while i in range(len(data) - 2):
    line1 = data[i]
    line2 = data[i + 1]
    line3 = data[i + 2]
    i += 3

    ch = '\0'

    st1 = set()
    st2 = set()

    for c in line1:
        st1.add(c)
    
    for c in line2:
        if c in st1:
            st2.add(c)
    
    for c in line3:
        if c in st2:
            ch = c
            break

    ans += dictOfItems[c]

print(ans)