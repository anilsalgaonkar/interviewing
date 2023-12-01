
def bubble(nums):
    for i in range(len(nums)):
        j = 0 
        while j < len(nums) - i -1:
            if nums[j]> nums[j+1]:
                nums[j], nums[j+1] =  nums[j+1], nums[j]
            j += 1
    return nums    

print(bubble([4,2,0,1,3,3,33,1,2]))
print(bubble([4,2,0,1,3,]))
print(bubble([4]))
