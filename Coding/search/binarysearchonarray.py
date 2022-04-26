def binary_search(arr: list, k: int ) -> int:
    left = 0
    right = len(arr)-1
    res = -1
    while left < right:
        mid = (left + right) // 2
        curr = arr[mid]
        if curr == k:
            return mid
        if curr < k:
            left = mid + 1
        else:
            right = mid -1 

    return res
        

arr = [1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222]
inputs = [10, 49, 99, 110, 176]

for i in inputs:
    print("result of searching " + str(i) + " ==> " + str(binary_search(arr,i)))
