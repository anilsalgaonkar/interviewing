def permutations(items):
  if not items:
    return [[]]

  first = items[0]
  remainingPerms = permutations(items[1:])
  fullPerms = []
  for perm in remainingPerms:
    for i in range(len(perm) + 1):  # +1 so that we have extra index to add after the last position 
      fullPerms.append([*perm[:i] ,first , *perm[i:]]) # insert  into array at ith position 
  return fullPerms


#print(permutations(['a','b','c']))


arr = [1,2,3]
arr = [*arr[:1], 1.1,1.2,1.3 , *arr[1:]]

print(*arr[1:], arr[:1])

for i in range(len(arr) + 1):
    print(*arr[:i], " -----", *arr[i:])
    #arr = [*arr[:i], 0 , *arr[i:]]
    #print(arr)