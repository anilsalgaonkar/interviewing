
def mergesort(input):
    #base case
    if len(input) <= 1:
        return input
    
    mid = len(input) // 2
    left = mergesort(input[:mid])
    right = mergesort(input[mid:])
    
    return merge(left, right)


def merge(left, right):
    out = []
    i , j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out += left[i:]
    out += right[j:]
    return out

import random
import time

st = time.time()
nums = [random.randint(1,100000) for _ in range(50000)]
#print(nums)

mergesort(nums)
et = time.time()
print("elapsed: ",et-st)
print(mergesort([1,4,2,3,6]))



def insertsort1(nums):

    for i in range(1,len(nums)):
        j = i-1
        while j >= 0 and nums[j+1]<nums[j]:
            nums[j], nums[j+1] =  nums[j+1], nums[j]
            j -= 1

    return nums

st = time.time()
nums = [random.randint(1,100000) for _ in range(50000)]
#print(nums)
nums2 = [x for x in range(50000,0,-1)]
#print(nums2)

insertsort1(nums2)
et = time.time()
print("elapsed: ",et-st)