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
    
    if v1 <= v3 and v2 >= v4:
        count += 1
        print(v1, v3, v2, v4)
    
    elif v1 >= v3 and v2 <= v4:
        count += 1
        print(v1, v3, v2, v4)
    
print(count)
    