from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            
            row = []
            col = []
            for j in range(9):
                
                #row check
                if board[i][j] != ".":
                    row.append(board[i][j])
                
                #col Check
                if board[j][i] != ".":
                    col.append(board[j][i])
                   
            if self.hasDuplicate(row):
                return False
            if self.hasDuplicate(col):
                return False
        
        for i in range(3):
            matrix = []
            for j in range(3):
                matrix = [board[3*i+r][3*j+c] for c in range(3) for r in range(3) if board[3*i+r][3*j+c] != "."]
                print(matrix)
                if self.hasDuplicate(matrix):
                    return False
        return True
        
        
    def hasDuplicate(self, nums):
        # print(nums)
        return len(set(nums)) != len(nums)
        

print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))