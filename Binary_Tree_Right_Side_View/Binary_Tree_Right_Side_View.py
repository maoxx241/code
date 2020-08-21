# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return 
        self.depth=-1
        def func(node,depth):
            if not node:
                return 
            if node:
                self.depth=max(self.depth,depth)
            func(node.left,depth+1)
            func(node.right,depth+1)
        
        def helper(node,depth,lst):
            if not node:
                return 
            
            if lst[depth]==-1:
                lst[depth]=node.val
            helper(node.right,depth+1,lst)
            helper(node.left,depth+1,lst)
        func(root,0)
        lst=[-1]*(self.depth+1)
        helper(root,0,lst)
        return lst
        