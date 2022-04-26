class Solution:
    def longestsubstring(self, s: str) -> int:
        seen = {}
        start = longest = 0

        for i,char in enumerate(s):   
            if char in seen and start <= seen[char]:
                start = seen[char] +1
            else:
                longest = max(longest, i-start+1)
            seen[char] = i
        return longest

print(Solution().longestsubstring("abcabcbb"))
print(Solution().longestsubstring("nameeeehhferytfs"))