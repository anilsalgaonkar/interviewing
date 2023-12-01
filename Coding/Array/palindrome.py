def ispalindrome(input):
    if not input:
        return True
    
    l = 0
    r = len(input)-1
    size = len(input)
    while l < r:
        if not input[r].isalnum():
            r -=1
            continue
        if not input[l].isalnum():
            l +=1
            continue
        if input[l].lower() != input[r].lower():
            return False
        l+=1
        r-=1
    return True

i1 = "A man, a plan, a canal: Panama"
i2 = "race a car"
print(ispalindrome(i1))
print(ispalindrome(i2))
print(ispalindrome("asa"))
