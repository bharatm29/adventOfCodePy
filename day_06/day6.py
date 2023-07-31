data = open("./input.txt").read()

myList = []

i = j = 0
size = len(data)
swl = 14
dick = dict()

while j < size:
    if data[j] not in dick:
        dick[data[j]] = 0
    dick[data[j]] += 1
    if len(dick) == j-i+1:
        if j-i+1 == swl:
            print(j+1)
            break
        j += 1
    else:
        while len(dick) < j-i+1:
            dick[data[i]] -= 1
            if dick[data[i]] == 0:
                dick.pop(data[i])
            i += 1
        j += 1