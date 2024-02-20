#https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_area = nums[0]
        curr_total = 0

        for n in nums:
            curr_total += n
            max_area = max(max_area, curr_total)

            if curr_total < 0:
                curr_total = 0  # reset to 0 only if the curr running total is -ve.  This is CRITICAL step.
        return max_area
        
        