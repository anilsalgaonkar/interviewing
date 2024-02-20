#
#https://www.youtube.com/watch?v=NA2Oj9xqaZQ

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return[[]]

        first = nums.pop(0)
        perms_without_first = self.permute(nums)
        all_perms = []
        for perm in perms_without_first:
            for i in range(len(perm)+ 1):
                perm_with_first = perm[:i] + [first] + perm[i:] # include first in each position.
                all_perms.append(perm_with_first)
        return all_perms
 
        