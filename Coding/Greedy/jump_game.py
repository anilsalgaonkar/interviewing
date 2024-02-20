#https://leetcode.com/problems/jump-game/description/

# the solution is simple but coming up with a solution is not easy.
# the idea is to move the goal in front iteratively if the goal can be reached from its left side num
# 
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) -1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
        