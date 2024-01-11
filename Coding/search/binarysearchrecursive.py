def binsearch(input,start,end,target):
    #base case
    if not input or start>end:
        return False

    mid = (end+start)//2
    
    if input[mid]==target:
        return True
    #recursive case
    return binsearch(input,mid+1,end,target) if target > input[mid] else binsearch(input,start,mid-1,target)

def search(input,target):
    return binsearch(input,0,len(input)-1,target)

print(search([5,6],5))
print(search([5,6],8))
print(search([5,6],3))