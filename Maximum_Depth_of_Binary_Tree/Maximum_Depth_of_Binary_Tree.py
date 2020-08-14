# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        self.ans=0
        def dfs(node,d):
            if not node:
                return 0
            self.ans=max(self.ans,d)
            dfs(node.left,d+1)
            dfs(node.right,d+1)
        
        dfs(root,1)
        return self.ans