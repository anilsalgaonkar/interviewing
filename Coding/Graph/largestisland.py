
def largestisland(graph):
    visited = set()
    maxsize = 0
    for node in graph:
        currsize = explore(graph,node,visited)
        maxsize = max(maxsize,currsize)
    return maxsize

def explore(graph, node, visited):

    if node in visited:
        return 0

    visited.add(node)
    count = 1
    for neigh in graph[node]:
        count += explore(graph, neigh, visited)

    return count
    


c = largestisland({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})

print(c)