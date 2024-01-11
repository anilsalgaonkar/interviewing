from collections import deque
def shortest_path(graph, src, tgt):

    q = deque([(0,src)])
    visited = set()
    while q:
        distance, node = q.popleft()
        visited.add(node)

        if node == tgt:
            return distance
        for neigh in graph[node]:
            if neigh not in visited:
                q.append((distance+ 1, neigh))
    return -1


# convert edges to adjacency list:
def create_graph(edges):
  g = {}
  for i, j  in edges:
    # if i not in g:
    #   g[i] = []
    # if j not in g:
    #   g[j] = []
    g[i] = g.get(i,[])
    g[j] = g.get(j,[])
    g[i].append(j)
    g[j].append(i)
  return g


edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v'],
  ['a', 'b']
]

print(shortest_path(create_graph(edges), 'w', 'a')) # -> -1
print(shortest_path(create_graph(edges), 'w', 'y')) # -> 2