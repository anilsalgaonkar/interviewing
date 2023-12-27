def quicksort(input,start,end):
    
    if not input or end - start + 1 <=1:
        return input
    
    pivot = input[end]
    left = start

    for i in range(start,end):
        if input[i] <= pivot:
            input[left], input[i] = input[i], input[left]
            left += 1
    input[left], input[end] = input[end], input[left]
    

    quicksort(input,start, left-1)
    quicksort(input,left+1, end)
    return input
    



print(quicksort([6,2,3,4,3],0,4))

import random, time
st = time.time()
nums1 = [random.randint(1,1000000) for _ in range(1000000)]
#print(nums1)
nums2 = [x for x in range(50000,0,-1)]
#print(nums2)

quicksort(nums1,0,len(nums1)-1)
et = time.time()
print("elapsed: ",et-st)