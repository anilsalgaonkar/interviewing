
def smallestisland(grid):
    smallest  = float("inf")
    visited = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            currsize = explore(row, col, grid, visited)
            if currsize > 0:
                smallest = min(smallest,currsize)
    return smallest

def explore(row, col, grid, visited):
    pos = (row,col)
    rowbound = (0 <= row < len(grid))
    colbound = (0 <= col < len(grid[0]))

    if not rowbound or not colbound:
        return 0
    
    if pos in visited:
        return 0

    if grid[row][col] == "W":
        return 0
    
    visited.add(pos)
    size = 1
    size += explore(row, col+1, grid, visited)
    size += explore(row, col-1, grid, visited)
    size += explore(row+1, col, grid, visited)
    size += explore(row-1, col, grid, visited)

    return size

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(smallestisland(grid)) # -> 2