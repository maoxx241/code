# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.value=0
        self.dif=float('inf') 
        if not root:
            return 
        def helper(node):
            if not node:
                return 
            if abs(node.val-target)<self.dif:
                self.dif=abs(node.val-target)
                self.value=node.val
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return self.value