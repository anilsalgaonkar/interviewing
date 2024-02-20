#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val > root.val and q.val > root.val:
            root = root.right
            return self.lowestCommonAncestor(root, p, q)

        if p.val < root.val and q.val < root.val:
            root = root.left
            return self.lowestCommonAncestor(root, p, q)
        
        return root