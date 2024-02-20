#https://leetcode.com/problems/palindromic-substrings/description/
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # odd length palindromes
            l, r = i,i
            count += self.count_palindrome(s,l,r)
 
             #even length palindromes
            l, r = i, i+1
            count += self.count_palindrome(s,l,r)
        return count
                
    
    def count_palindrome(self, s: str, l: int, r: int) -> int:
        count = 0
        while l>=0 and r<len(s) and s[l]==s[r]:
            l -= 1
            r += 1
            count += 1
        return count
        

print(Solution().countSubstrings("babad"))
