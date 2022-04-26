from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        #swap the children
        tmp = root.right
        root.right = self.invertTree(root.left) 
        root.left = self.invertTree(tmp)
        return root 


def printInOrder(node: TreeNode):
    if(node):
        printInOrder(node.left)
        print(node.val)
        printInOrder(node.right)

def printPreOrder(node: TreeNode):
    if(node):
        print(node.val)
        printPreOrder(node.left)
        printPreOrder(node.right)



t1 = TreeNode(0,TreeNode(1,None,None),TreeNode(2,TreeNode(3,None,None),TreeNode(4,None,None)))
t2 = TreeNode(0,TreeNode(1,None,None),TreeNode(2,TreeNode(2,None,None),TreeNode(4,None,None)))

it1 = Solution().invertTree(t1)
printPreOrder(it1)