# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans=0
        def search_BST(node):
            if not node:
                return
            if L<=node.val<=R:
                self.ans+=node.val
            if L < node.val:
                    search_BST(node.left)
            if node.val < R:
                    search_BST(node.right)
        
        search_BST(root)
        return self.ans