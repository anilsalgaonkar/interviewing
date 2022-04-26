from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root :
            return False
        if root.val == subRoot.val and self.isSameTree(root.left,subRoot.left) and self.isSameTree(root.right,subRoot.right):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False   
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)  



t1 = TreeNode(3,TreeNode(4,TreeNode(1,None,None),TreeNode(2,None,None)),TreeNode(5,None,None))
t2 = TreeNode(0,TreeNode(1,None,None),TreeNode(2,TreeNode(2,None,None),TreeNode(4,None,None)))
t3 = TreeNode(1,TreeNode(1,None,None),None)
t4 = TreeNode(1,None,None)

print(Solution().isSubtree(t3,t4)) 
