
#recursive
def has_path(graph, src, tgt):
    if src is None and tgt:
        return False

    if src == tgt:
        return True
    
    for node in graph[src]:
        if has_path(graph,node,tgt):
            return True
    return False


graph = {
'f': ['g', 'i'],
'g': ['h'],
'h': [],
'i': ['g', 'k'],
'j': ['i'],
'k': []
}

print(has_path(graph, 'g', 'k') )