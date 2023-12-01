#https://leetcode.com/problems/concatenation-of-array/
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0]*n* 2
        print(ans)
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        
        return ans


    def getConcatenation1(self, nums):
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans

print(Solution().getConcatenation1([1,2,5,6,7,8]))