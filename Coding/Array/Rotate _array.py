#https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  #. critical step to restrict k with len(nums)
        break_point = len(nums) - k

        self.reverse(nums, 0, break_point - 1)
        self.reverse(nums, break_point, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
    
    def reverse(self, nums, left, right):
         while left < right:
            nums[left], nums[right] = nums[right] , nums[left]

            left += 1
            right -= 1
        