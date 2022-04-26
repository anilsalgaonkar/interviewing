def max_path_sum(grid, r, c):
    return _max_path_sum(grid,0,0,{})

def _max_path_sum(grid, r, c, memo):
    rowbound, colbound = len(grid)-1, len(grid[0])-1

    pos = r,c
    if pos in memo:
        return memo[pos]
    if pos == (rowbound,colbound):
        return grid[r][c]

    if  r > rowbound or c > colbound:
        return float("-inf")
    
    maxsum = float("-inf")

    downsum = grid[r][c] + _max_path_sum(grid,r+1,c,memo)
    rightsum = grid[r][c] + _max_path_sum(grid,r, c+1, memo)
    maxsum  = max(downsum,rightsum, maxsum)

    memo[pos] = maxsum
    return maxsum
    



grid = [
  [1, 3, 12],
  [5, 1, 1],
  [3, 6, 1],
]

print(max_path_sum(grid,0,0))