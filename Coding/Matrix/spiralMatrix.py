#https://leetcode.com/problems/spiral-matrix/

def spiralOrder(matrix):

    left = 0
    right  = len(matrix[0])
    top = 0
    bottom = len(matrix)
    res = []
    while left < right and top < bottom:

        # top row
        for i in range(left,right):
            res.append(matrix[top][i])
        top += 1

        # right column
        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -= 1

        print(top,bottom, left, right)
        if not (left < right and top < bottom):
            break

        # bottom row
        for i in range(right - 1, left-1, -1):
            res.append(matrix[bottom-1][i])
        bottom -= 1

        # left colimn
        for i in range(bottom - 1, top-1, -1):
            res.append(matrix[i][left])
        left += 1

    return res



matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))