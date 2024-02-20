# https://leetcode.com/problems/rotting-oranges/submissions/1179204156/

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        queue = deque([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_count += 1 
                elif grid[r][c] == 2:
                    queue.append((r,c,0))
        
        return self.count_mins(grid,fresh_count, queue) if fresh_count > 0 else 0

    def count_mins(self, grid, fresh_count, queue):
        dir = [[1,0],[0,1],[-1,0],[0,-1]]

        while queue:
            r, c, mins =  queue.popleft()
            #print(r,c,mins,fresh_count,queue)
            for i,j in dir:
                row = r + i
                col = c + j
                if  0 <= row < len(grid) and 0 <= col < len(grid[0]):
                    if grid[row][col] == 1:
                        queue.append((row,col,mins + 1))
                        fresh_count -= 1
                        grid[row][col] = 2
                        if fresh_count == 0:
                            return mins + 1
        return -1

            

        