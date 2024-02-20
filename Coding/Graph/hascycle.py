def has_cycle(graph):
    memo = set()  # cache
    for node  in graph:
        if explore(node,graph, set(), memo):
            return True
    return False

def explore(node, graph,visiting, memo):

    if node in visiting:
        return True

    if node in memo:
        return False

    visiting.add(node)
    for neigh in graph[node]:
        if explore(neigh, graph, visiting, memo):
            return True
    visiting.remove(node)
    memo.add(node)

    return False

     



print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
})) # -> True


print(has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
})) # -> False

print(has_cycle({
  "q": ["r", "s"],
  "r": ["t", "u"],
  "s": [],
  "t": [],
  "u": [],
  "v": ["w"],
  "w": [],
  "x": ["w"],
})) # -> False