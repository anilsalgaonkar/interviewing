from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False   
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


t1 = TreeNode(0,TreeNode(1,None,None),TreeNode(2,TreeNode(2,None,None),TreeNode(4,None,None)))
t2 = TreeNode(0,TreeNode(1,None,None),TreeNode(2,TreeNode(2,None,None),TreeNode(4,None,None)))

print(Solution().isSameTree(t1,t2)) 


p =  q = None
print(Solution().isSameTree(t2,q)) 