
def countisland(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph,node,visited):
            count += 1
    return count

def explore(graph, node, visited):

    if node in visited:
        return False

    visited.add(node)

    for neigh in graph[node]:
        explore(graph, neigh, visited)

    return True
    


c = countisland({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})

print(c)