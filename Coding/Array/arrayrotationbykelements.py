
def rotate(arr,k):
    n = len(arr)
    arr[:n-k]= arr[:n-k:-1]




def reverse(arr, l, r):

    #l = 0
    #r = len(arr)-1

    while l <= r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    
    return arr

arr = [1,2,3,4,5]
print(reverse(arr,0, 2))



