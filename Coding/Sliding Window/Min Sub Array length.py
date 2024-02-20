# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1115184139/
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        length =  float('inf')
        arraysum = 0     

        for r in range(len(nums)):
            arraysum += nums[r]

            while arraysum >= target:
                length = min(length, r-l+1)
                #print(arraysum,length,r, l , r-l+1)
                arraysum -= nums[l]
                l +=1
        return 0 if length == float('inf') else length


#print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))

        