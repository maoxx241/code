# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         ans=slow=ListNode(0)
#         slow.next=l1
#         while l1 and l2:
#             if l1.val+l2.val>9:
#                 slow.val+=1
#             l1.val=(l1.val+l2.val)%10
#             l1=l1.next
#             l2=l2.next
#             if slow.next:
#                 slow=slow.next
        
#         if l2:
#             slow.next=l2
        
#         if ans.val==1:
#             return ans
#         else:
#             return ans.next
        if not l1 and not l2:
            return None

        l1_num = 0
        while l1:
            l1_num = l1_num * 10 + l1.val
            l1 = l1.next

        l2_num = 0
        while l2:
            l2_num = l2_num * 10 + l2.val
            l2 = l2.next

        lsum = l1_num + l2_num

        head = ListNode(None)
        cur = head
        for istr in str(lsum):
            cur.next = ListNode(int(istr))
            cur = cur.next

        return head.next