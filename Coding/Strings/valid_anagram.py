'''
242. Valid anagram

https://leetcode.com/problems/valid-anagram/

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


    def isAnagram1(self, s: str, t: str) -> bool:
        sdic, tdic  = {}, {}
        for char in s:
            sdic[char] = sdic.get(char,0) + 1
        for char in t:
            tdic[char] = tdic.get(char,0) + 1
        return sdic == tdic
    
    def isAnagram2(self, s:str , t:str) -> bool:
        return set(s) == set(t)

        


print(Solution().isAnagram2("abc","asd"))