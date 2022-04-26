class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        #base case
        if not root:
            return 0
        return 1 + max( self.maxDepth(root.left), self.maxDepth(root.right))

root = TreeNode(0,TreeNode(1,None,None),TreeNode(2,TreeNode(3,None,None),TreeNode(4,None,None)))
print(Solution().maxDepth(root))
root = TreeNode(None,None,None)
print(Solution().maxDepth(root))
root = None
print(Solution().maxDepth(root))