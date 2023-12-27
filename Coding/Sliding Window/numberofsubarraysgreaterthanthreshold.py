#https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/submissions/1114655855/

class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        count = 0
        sum = 0
        l = 0
        for r, val in enumerate(arr):
            if r -l +1 > k:
                if sum >= threshold * k:
                    count += 1
                sum -= arr[l]
                l += 1 
            sum += val
        
        if sum >= threshold * k:
            count += 1
        return count