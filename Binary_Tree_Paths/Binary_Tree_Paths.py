# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.ans=[]
        def helper(node,string):
            if not node:
                return 
            if not node.left and not node.right:
                self.ans.append((string+ "->" + str(node.val))[2:])
                return 
            
            helper(node.left,string + "->" + str(node.val))
            helper(node.right,string + "->" + str(node.val))
        
        if not root:
            return []
        helper(root,"")
        return self.ans