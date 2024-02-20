#https://leetcode.com/problems/subsets/description/


#recursion
def subsets(nums):
    if not nums:
        return[[]]

    first = nums.pop(0)
    combs_without_first = subsets(nums)
    combs_with_first = []
    for comb in combs_without_first:
        combs_with_first.append([first] + comb.copy())
    return combs_with_first + combs_without_first

# bactracking technique
def subsets1(nums):
    res = []
    subset = []
    explore(0,res,nums,subset)
    return res

def explore(i, res, nums, subset):
    if i >= len(nums):
        res.append(subset.copy())   # << == copying the array instead of passing . can also do subset[:] 
        return
    # decision to include nums[i]
    subset.append(nums[i])
    explore(i + 1,res, nums, subset)

    # decision NOT to include nums[i]
    subset.pop()
    explore(i + 1,res, nums, subset)

print(subsets([1,2,3]))