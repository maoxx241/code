# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x=0
        self.y=0
        self.x_p=None
        self.y_p=None
        def helper(p,node,depth,x,y):
            if not node:
                return
            if node.val==x:
                self.x=depth
                self.x_p=p
                return
            if node.val==y:
                self.y=depth
                self.y_p=p
                return
            helper(node,node.left,depth+1,x,y)
            helper(node,node.right,depth+1,x,y)
        
        helper(None,root,0,x,y)
        return self.x==self.y and self.x_p!=self.y_p