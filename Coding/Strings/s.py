'''
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

'''

class Solution:
    def isValid(self, s: str) -> bool:
        s.replace(' ','')
        
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()','').replace('{}','').replace('[]','')

        if s=='':
            return True
        else:
            return False

Solution().isValid("({})()")