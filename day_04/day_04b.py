data = open("./input.txt").read().split('\n')

count = 0

for line in data:
    nums = []
    pairs = line.split(',')
    
    nums1 = pairs[0].split('-')
    nums2 = pairs[1].split('-')
    
    v1 = int(nums1[0])
    v2 = int(nums1[1])
    v3 = int(nums2[0])
    v4 = int(nums2[1])
    
    numer1 = []
    
    for i in range(v1, v2+1):
        numer1.append(i)
    
    for i in range(v3, v4+1):
        if i in numer1:
            count += 1
            break
    
print(count)
    

