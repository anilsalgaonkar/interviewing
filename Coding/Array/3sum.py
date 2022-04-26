
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    sumlist = []
    sumliststr = []
    nums = sorted(nums)
    print(nums)
    for i,inum in enumerate(nums):
        left = i+1
        right = len(nums)-1
        while(left < right):
            
            triplet = [inum , nums[left] , nums[right]]
            tripletstr = "".join(map(str, triplet))
            tripletsum = inum + nums[left] + nums[right]


            if tripletsum == 0:
                if tripletstr not in sumliststr:
                    sumlist.append(triplet)
                    sumliststr.append(tripletstr)
                left += 1
                right -= 1 
            elif tripletsum < 0:
                left += 1
            elif tripletsum >0:
                right -= 1 
    return sumlist

print(threeSum([-1,0,1,2,-1,-4]))      