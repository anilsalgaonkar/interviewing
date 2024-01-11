#https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/submissions/1114655855/

class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
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

    def numOfSubarrays2(self, arr, k, threshold):
        count = 0 
        sum = sum(arr[:k])
        if sum >= threshold * k:
            count += 1

        for i in range(len(arr)-k):
            sum += arr[i+k]
            sum -= arr[i]
            if sum >= threshold * k:
                count += 1
        
        return count


