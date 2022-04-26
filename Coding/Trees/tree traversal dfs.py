class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#using recursion. print the list and also return the list
def depthfirsttraversal(root) -> list:
    if not root: 
        return None
    
    print(root.val)
    res  = [root.val]
    left  = depthfirsttraversal(root.left)
    if left:
        res = res + left
    right  = depthfirsttraversal(root.right)
    if right:
        res = res + right
    
    return res
    

t2 = TreeNode(0,TreeNode(1,TreeNode(11,None,None),TreeNode(12,None,None)),TreeNode(2,TreeNode(21,None,None),TreeNode(22,None,None)))


print(depthfirsttraversal(t2))

#using iterative solution. use stack to traverse the node, pop  the node just traversed and add its children on the stack
def depthfirsttraversaliterative(root) -> list:
    if not root: 
        return None
    
    stack = [root]

    while stack:
        cur  = stack.pop()
        print(cur.val)
        if cur.right: # right is added first 
            stack.append(cur.right)
        if cur.left: # left is added later so it can be traversed first.
            stack.append(cur.left)
    

depthfirsttraversaliterative(t2)