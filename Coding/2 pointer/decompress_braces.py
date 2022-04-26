# this has O(n^2) 
# can you improve it ?

def evaluate(s):
    
    factors = []
    values = []
    factor = 0
    value = ""
    for c in s:
        
        #keep on building until you find [
        if c.isnumeric():
            factor = factor * 10 + int(c)

        # if you find put it on the stack  to get  the latest number when we want to multiply, reset factor
        elif c == '[':
            factors.append(factor)
            factor = 0
        
        # when you do find ] multiply factor by evaluted string  and push on the result on to the  stack, reset value
        elif c == ']':
            poppedvalue = values.pop() if values else ""
            values.append(factors.pop() * (poppedvalue + value))
            value = ""


        else:
            value += c
    return values.pop()

print(evaluate("3[2[ab]]"))    #abab abab abab

print(evaluate("3[1[a]2[bc]]"))    # abcbc abcbc abcbc




def decode(s):
    if '[' not in s:
        return s

    i = j = 0
    num = ""
    stack = []
    out = []
    while j < len(s):
        if s[j] == '[':
            if not stack:
                num = s[i:j]
                i = j+1
            stack.append('[')

        if s[j] == ']':
            stack.pop()
            if not stack:
                out.append(int(num) * decode(s[i:j]))
                i = j+1
        j += 1
    return "".join(out)

s1 = "3[2[3[4[a]]]]" #- > aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
print(decode(s1))


s2 = "3[1[a]2[bc]]" #-> abcbcabcbcabcbc
print(decode(s2))


s = "123"
num = 0
for n in s:
    num = num * 10 + int(n)

print(num)
