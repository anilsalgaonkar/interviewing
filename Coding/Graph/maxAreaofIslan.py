#https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        visited = set() # maintain a list of visited cells
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    currArea  = self.explore(r,c, grid, visited)  
                    maxArea = max(maxArea,currArea)
        return maxArea



    def explore(self, r, c, grid, visited):
        row_bounds = 0 <= r < len(grid)
        col_bounds = 0 <= c < len(grid[0])

        # check to make sure blunds are not crossed
        if not row_bounds or not col_bounds:
            return 0

        # water is not counted
        if grid[r][c] == 0:
            return 0
        
        # do not double count visited cells.
        if (r,c) in visited: 
            return 0

        visited.add((r,c))
        count = 1

        count += self.explore(r+1,c, grid, visited)
        count += self.explore(r-1,c, grid, visited)
        count += self.explore(r,c+1, grid, visited)
        count += self.explore(r,c-1, grid, visited)

        return count


