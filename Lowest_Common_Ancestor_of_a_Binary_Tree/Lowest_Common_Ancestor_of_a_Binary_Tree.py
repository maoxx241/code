# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def recurse_tree(node):

            # If reached the end of a branch, return False.
            if not node:
                return False

            # Left Recursion
            left = recurse_tree(node.left)

            # Right Recursion
            right = recurse_tree(node.right)

            # If the current node is one of p or q
            mid = node == p or node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = node

            # Return True if either of the three bool values is True.
            return mid or left or right
        
        recurse_tree(root)
        return self.ans