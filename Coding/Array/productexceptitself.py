def productExceptSelf(nums):
    prefix = 1
    postfix = 1
    res = [1]
    for i in range(len(nums) -1):
        res.append(prefix * nums[i])
        prefix = nums[i] * prefix
        print(res, prefix)
    
    for i in range(len(nums) - 1, -1, -1):
        res[i] = postfix * res[i]
        postfix = postfix * nums[i]
    return res

print(productExceptSelf([1,2,3,4]))