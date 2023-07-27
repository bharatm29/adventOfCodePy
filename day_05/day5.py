myInput = open("C:/Home/misc/data/dev/adventOfCodePy/day_05/input.txt").read().split('\n')
list1 = ['J','F','C','N','D','B','W']
list2 = ['T','S','L','Q','V','Z','P']
list3 = ['T','J','G','B','Z','P']
list4 = ['C','H','B','Z','J','L','T','D']
list5 = ['S','J','B','V','G']
list6 = ['Q','S','P']
list7 = ['N','P','M','L','F','D','V','B']
list8 = ['R','L','D','B','F','M','S','P']
list9 = ['R','T','D','V']

lsList = [list1, list2, list3, list4, list5, list6, list7, list8, list9]

for i in lsList:
    i.reverse()

for line in myInput:
    inst = line.split(' ')
    size = int(inst[1])
    src = int(inst[3]) - 1
    dest = int(inst[5]) - 1
    for j in range(0, size):
        if lsList[src] != []:
            temp = lsList[src][-1]
            lsList[src].pop()
        lsList[dest].append(temp)

for i in lsList:
    print(i[-1])