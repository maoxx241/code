# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        lst=head
        while lst and lst.next:
            if lst.val == lst.next.val:
                lst.next=lst.next.next
            else:
                lst=lst.next
        
        return head