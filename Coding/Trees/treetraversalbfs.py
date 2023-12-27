class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#using iterative. print the list and also return the list. very difficult to write recursive solution for BFS
def breadthfirsttraversal(root) -> list:
    if not root:
        return None
    
    queue  = [root]
    res = []
    while queue:
        cur = queue.pop(0)
        print(cur.val)
        res.append(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return res

# recursive solution except it does not traverse the root node.
def bfs(root):
    if not root:
        return None
    if root.left:
        print(root.left.val)
    if root.right:
        print(root.right.val)
    bfs(root.left)
    bfs(root.right)




from collections import deque
def bfsiterative(root):
    if not root:
        return None
    q = deque([root])

    while q:
        curr = q.popleft()
        if curr:
            print(curr.val)
            q.append(curr.left)
            q.append(curr.right)




t2 = TreeNode(0,TreeNode(1,TreeNode(12,None,None),TreeNode(13,None,None)),TreeNode(2,TreeNode(21,None,None),TreeNode(22,None,None)))
print(breadthfirsttraversal(t2))

bfs(t2)
print("\n")
bfsiterative(t2)