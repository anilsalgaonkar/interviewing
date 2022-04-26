from collections import Counter
class Solution:

    #This was my solution but it does not work.
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        if len(s) < len(t): return ""
        
        countert = Counter(t)
        counters = Counter(s)

        for c in t:
            if counters[c] < countert[c]:
                return ""
               
        shortest = len(s)
        minsubstr = {shortest:s}
        l , r = 0, len(s)-1
        
        for i in range(len(s)-len(t) +1):
            counters[s[i]] -= 1
            if s[i] in t and counters[s[i]] < countert[s[i]]:
                shortest = min(shortest, r-i+1)
                minsubstr[shortest] = minsubstr.get(shortest,s[i:r+1])
                break
        
        countert = Counter(t)
        counters = Counter(s)
        for i in range(len(s)-1, -2 + len(t), -1):
            counters[s[i]] -= 1
            if s[i] in t and counters[s[i]] < countert[s[i]]:
                shortest = min(shortest, i-l)
                minsubstr[shortest] = minsubstr.get(shortest,s[l:i+1])
                break
        return minsubstr[shortest]


    def minWindow1(self,s: str, t: str) -> str:
        if t == "": return ""
        if len(s) < len(t): return ""
        countt, cwindow = Counter(t) , {}
        
        minstr = [0,0]
        minstrlen = float("infinity")
        need, have, l = len(countt), 0, 0

        for r, c in enumerate(s):
            cwindow[c] = cwindow.get(c,0) + 1

            if c in countt and cwindow[c] == countt[c]:                    
                have += 1

            # while have is equal to need, keep on updating minlen and minstr until it no longer true.
            # this the sliding window condition, which changes/slides the window. Need is fixed, the only thing that c
            #can change is the have which is dependent on the input string.
            while have == need:
                # update the result
                if r - l + 1 < minstrlen:
                    minstr = [l, r]
                    minstrlen = r-l + 1

                # pop from left of our window . This is the changing/breaking condition for while loop
                cwindow[s[l]] -= 1
                if s[l] in countt and cwindow[s[l]] < countt[s[l]]:
                    have -= 1
                l += 1
        l, r = minstr
        return s[l:r+1] if minstrlen != float("infinity") else "" 

                    
                    


print(Solution().minWindow1("AA","AA"))