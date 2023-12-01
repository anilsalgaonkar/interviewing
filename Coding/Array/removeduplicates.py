#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums

        #remove duplicates
        prev = 0
        i = 1
        while i < len(nums): 
            if nums[prev] == nums[i]:
               # nums.pop(i)
               nums[i]= "_"
               i+=1
            else:
                prev = i
                i+=1

        #rearrange
        u = -1
        j = -1
        i = 0
        while i < len(nums):
            if nums[i]=="_":
                u = i
                j = i+1
                while j<=len(nums)-1 and nums[j] != "_":
                    j+=1
                #swap
                print(i,u, j)
                nums[u] = nums[j]
                nums[j] = "_"
            i+=1 
        
        return nums

    def removedup(self,nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l +=1
        return l
    






                



nums = [1,1,2]

nums1 = [0,0,1,1,1,2,2,3,3,4]

assert Solution().removedup(nums) == 2 
assert Solution().removedup(nums1) == 5

import unittest
 
class TestRD(unittest.TestCase):

    def test_removeDup(self):
        self.assertEqual(Solution().removedup([1,1,2]),2)
        self.assertEqual(Solution().removedup([0,0,1,1,1,2,2,3,3,4]),5)


unittest.main()