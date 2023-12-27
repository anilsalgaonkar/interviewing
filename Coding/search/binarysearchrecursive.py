def binsearch(input,start,end,target):
    #base case
    if not input or end-start+1<1:
        return False

    mid = (end+start)//2
    
    if input[mid]==target:
        return True
    #recursive case
    elif target > input[mid]:
        return binsearch(input,mid+1,end,target)
    else:
        return binsearch(input,start,mid,target)

def search(input,target):
    return binsearch(input,0,len(input)-1,target)

print(search([5,6],7))