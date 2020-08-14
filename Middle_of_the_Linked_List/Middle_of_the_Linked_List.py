# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        if fast.next == None:
            return slow
        return slow.next