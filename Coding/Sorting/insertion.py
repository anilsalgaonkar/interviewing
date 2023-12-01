
def insertsort(nums):

    for i in range(1,len(nums)):
        j = i-1
        while j >= 0 and nums[j+1]<nums[j]:
            nums[j], nums[j+1] =  nums[j+1], nums[j]
            j -= 1

    return nums


print(insertsort([4,2,0,1,3,3,33,1,2]))
print(insertsort([4,2,0,1,3,]))
print(insertsort([4,2,0,1222]))
print(insertsort([4,2]))
print(insertsort([4]))
        

