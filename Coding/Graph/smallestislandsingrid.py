
def smallestisland(grid):
    smallest  = float("inf")
    visited = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            currcount = explore(row, col, grid, visited)
            if currcount > 0:
                smallest = min(smallest,currcount)
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
    count = 1
    count += explore(row, col+1, grid, visited)
    count += explore(row, col-1, grid, visited)
    count += explore(row+1, col, grid, visited)
    count += explore(row-1, col, grid, visited)

    return count

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(smallestisland(grid)) # -> 2