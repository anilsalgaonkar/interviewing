#https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0 
        total = sum(arr[:k])
        if total >= threshold * k:
            count += 1

        for i in range(len(arr)-k):
            total += arr[i+k]
            total -= arr[i]
            if total >= threshold * k:
                count += 1
        
        return count