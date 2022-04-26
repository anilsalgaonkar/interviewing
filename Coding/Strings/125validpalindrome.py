class Solution:
    def isValid(self, s: str) -> bool:
        # use filter to get alph numeric chars only. Filter returns an iterator
        #alpnums = filter(str.isalnum,s)

        # this does the same thing
        alpnums = (c for c in s if str.isalnum(c))

        # iterate through iterator using join and convert to string and then change to lowercase
        alpnums = ''.join(alpnums).lower()
        print(alpnums + " " + alpnums[::-1])
        return alpnums[::-1] == alpnums
   


#all the above code can be compressed in 2 lines
    def isValid2(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]
        

print(Solution().isValid("bababa"))