#https://leetcode.com/problems/search-a-2d-matrix/

def solution(matrix,target):

    return search(matrix,target)

def search(matrix,target):
    if not matrix:
        return False

    rs = 0
    re = len(matrix)-1
    cs = 0
    ce = len(matrix[0])-1
    
    while rs<=re and cs<=ce:
        if rs != re:
            midrow = (rs+re)//2
            midrowstartval = matrix[midrow][cs]
            midrowendval = matrix[midrow][ce]
            if target == midrowstartval or target == midrowendval:
                return True
            elif target > midrowendval:
                rs = midrow + 1
            elif target < midrowstartval:
                re = midrow - 1
            else:
                rs = midrow
                re = midrow
        else:
            midcol = (cs + ce)//2
            midcolval = matrix[rs][midcol]
            if target == midcolval:
                return True
            elif target > midcolval:
                cs = midcol + 1
            else:
                ce = midcol -1

    return False




print(solution(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(solution(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
print(solution(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 23))

