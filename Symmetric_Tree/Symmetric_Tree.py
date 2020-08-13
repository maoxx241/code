# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        self.ans=True
        def dfs(left,right):
            if not left and not right:
                return 
            if not left or not right:
                self.ans=False
                return 
            if left.val != right.val:
                self.ans = False
            dfs(left.right,right.left)
            dfs(left.left,right.right)
        
        dfs(root.left,root.right)
        return self.ans