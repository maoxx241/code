# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.lst=[]
        def helper(node):
            if not node:
                return
            helper(node.left)
            self.lst.append(node.val)
            helper(node.right)
        helper(root)
        self.index=-1

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index+=1
        return self.lst[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.index<len(self.lst)-1 else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()