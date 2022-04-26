
def numisland(grid):
    count = 0
    visited = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(row, col, grid, visited):
                count += 1
    return count

def explore(row, col, grid, visited):
    pos = (row,col)
    rowbound = (0 <= row < len(grid))
    colbound = (0 <= col < len(grid[0]))

    if not rowbound or not colbound:
        return False
    
    if pos in visited:
        return False

    if grid[row][col] == "W":
        return False
    
    visited.add(pos)

    explore(row, col+1, grid, visited)
    explore(row, col-1, grid, visited)
    explore(row+1, col, grid, visited)
    explore(row-1, col, grid, visited)

    return True

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(numisland(grid)) # -> 3