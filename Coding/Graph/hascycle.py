def has_cycle(graph):
    complete = set()
    for node  in graph:
        if _hascycle(node,graph, set(), complete):
            return True
    return False

def _hascycle(node, graph,visiting, complete):

    if node in visiting:
        return True

    if node in complete:
        return False

    visiting.add(node)
    for neigh in graph[node]:
        if _hascycle(neigh, graph, visiting, complete):
            return True
    visiting.remove(node)
    complete.add(node)

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