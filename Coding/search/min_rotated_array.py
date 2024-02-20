'''
M
Find Minimum in Rotated Sorted Array
 https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''

def min_in_rotated_array(nums):
    left = 0
    right = len(nums)-1
    while nums[left] > nums[right]:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left= mid +1
    print (left, right)
    return nums[left]


print(min_in_rotated_array([4,5,6,7,2,3]))
print(min([4,5,6,7,2,3]))