#

def longestNiceSubarray(nums):
    if len(nums)==1:
        return 1

    length = 0


    for r in range(1,len(nums)):

        if nums[r]&nums[r-1] != 0:
            l = r
        else:
            length = max(length, r-l)
    return 1 if length == 0 else length

nums = [744437702,379056602,145555074,392756761,560864007,934981918,113312475,1090,16384,33,217313281,117883195,978927664]
for i in range(len(nums) - 1):
    print(nums[i]&nums[i+1])
print(longestNiceSubarray(nums))