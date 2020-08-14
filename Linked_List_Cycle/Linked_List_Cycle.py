# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         dic={}
#         while head:
#             if head not in dic:
#                 dic[head]=head.next
#                 head=head.next
#             else:
#                 return True
        
#         return False
        
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast=slow=head
        while fast and slow and fast.next:
            fast=fast.next.next
            slow=slow.next
            
            if fast == slow:
                return True
        
        return False