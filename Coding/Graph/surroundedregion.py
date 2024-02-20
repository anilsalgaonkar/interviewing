#https://leetcode.com/problems/surrounded-regions/description/
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r,c) not in visited:
                    is_valid, cells = self.capture_region(board, r, c, visited)
                    if is_valid and cells:
                        print(is_valid, cells)
                        self.flip(cells, board)
                        
        return board

    def capture_region(self, board, r, c, visited):
        row_bounds = 0 <= r < len(board)
        col_bounds = 0 <= c < len(board[0])

        if not row_bounds or not col_bounds:
            return (False,[])

        if (r,c) in visited:
            return (True, [])
        
        if board[r][c] == 'X':
            return (True, [])
        

        visited.add((r,c))
        
        top, tc = self.capture_region(board, r+1, c, visited)
        bottom, bc = self.capture_region(board, r-1, c, visited)
        right, rc = self.capture_region(board, r, c+1, visited)
        left, lc = self.capture_region(board, r, c-1, visited)

        if top and bottom and left and right : # return True if surrounded by all sides
            cells = [(r,c)]
            cells.extend(tc)
            cells.extend(bc)
            cells.extend(lc)
            cells.extend(rc)
            return True, cells
        else:
            return False, []


    def flip(self, cells, board):
        for r,c in cells:
            board[r][c] = 'X'