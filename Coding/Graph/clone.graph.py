#https://leetcode.com/problems/clone-graph/description/


# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        visited = {}
        return self.clone(node, visited) if node else None

    def clone(self, node, visited):
        if not node:
            return []

        if node in visited:
            return visited[node]
        
        visited[node] = Node(node.val)
        copy = visited[node]
        for n in node.neighbors:
            copy.neighbors.append(self.clone(n,visited))

        return copy
        