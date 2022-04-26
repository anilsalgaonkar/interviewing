from collections import deque
def shortestpath(grid, startpos):
    visited= set()
    return explore(grid,startpos,visited)

def explore(grid,pos,visited):
    
    
    q = deque([(0,pos)])
    while q:
        distance, pos = q.popleft()
        r, c = pos
        if (not 0 <= r < len(grid)) or (not 0 <= c < len(grid[0])):  # row and col bounds constraint
            continue
        
        if grid[r][c] == 'X': # X constraint
            continue

        if pos in visited: # visited constraint
            continue

        if grid[r][c] == "C":
            return distance

        visited.add(pos)

        q.append((distance+1,(r,c+1)))
        q.append((distance+1,(r,c-1)))
        q.append((distance+1,(r+1,c)))
        q.append((distance+1,(r-1,c)))



    return -1






grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

print(shortestpath(grid, (1, 2)))