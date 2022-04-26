
def insert(intervals, I):
    '''
    This has O(n) time complexity
    '''
    res, i = [], -1
    for i, (x, y) in enumerate(intervals):
        if y < I[0]:
            res.append([x, y])
        elif I[1] < x:
            i -= 1
            break
        else:
            I[0] = min(I[0], x)
            I[1] = max(I[1], y)
            
    out = res + [I] + intervals[i+1:]
    return out 

def insertbinary(intervals, I):
    '''
    trying to solve using O(nlogn) complexity
    '''
    # todo edge case for len 0 and 1
    if len(intervals) == 0:
        return [I]
    if len(intervals) == 1:
        return [[min(I[0],intervals[0][0]), max(I[1], intervals[0][1])]]


    overlapstartindex = 0
    
    start = 0
    end = len(intervals)-1
    while start <= end:
        mid = (end + start) // 2
        if I[0] < intervals[mid][0]:
            end = mid -1
        elif I[0] > intervals[mid][1]:
            start = mid +1
        else:
            I[0] = min(I[0],intervals[mid][0])
            overlapstartindex = mid
            break
    overlapendindex = overlapstartindex
    for i in range(overlapstartindex, len(intervals)):
        if I[1] < intervals[i][0]:
            overlapendindex = i-1
            break
    I[1] = max(I[1],intervals[overlapendindex][1])
    res = intervals[0:overlapstartindex] + [I] + intervals[overlapendindex+1:]
    return res

print(insertbinary([[1,5]],[6,8]))
print(insert([[1,5]],[6,8]))
