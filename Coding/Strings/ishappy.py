
def is_happy(instr):
    print(instr)
    count = {}
    happy = True
    for ch in instr:
        if ch in count:
            count[ch] = count[ch] + 1 
        else:
            count[ch] = 1
    happy = True
    for ch,val in count:
        if ch < 2:
            return False
        elif ch
        
  

while True:
    inp = input("Input: ")
    print(is_happy(inp))

