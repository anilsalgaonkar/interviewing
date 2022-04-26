class Solution:
    def isValid(self, s: str) -> bool:
        closer = {")":"(", "}":"{", "]":"["}
        stk = []
        
        for c in s:
            if stk and c in closer and stk[-1] == closer[c]:
                stk.pop()
            else:
                stk.append(c)
        
        # these 4 lines can be replaced by just 1 line --> 
        return stk == []
        '''
        if not stk: 
            return True
        else:
            return False
        '''


    def isValid2(self, s):
        stack = []
        closer = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in closer.values():
                stack.append(char)
            elif char in closer.keys():
                if stack == [] or closer[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
        

print(Solution().isValid("()[]{}"))