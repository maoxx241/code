# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy=cur=ListNode(0)
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        for i in range(0,len(lst),2):
            if i+1==len(lst):
                break
            temp=lst[i]
            lst[i]=lst[i+1]
            lst[i+1]=temp
        for i,n in enumerate(lst):
            cur.next=ListNode(n)
            cur=cur.next
        return dummy.next




    # def swapPairs(self, head):
    #     dummy = pre = ListNode(0)
    #     pre.next = head
    #     while pre.next and pre.next.next:
    #         a = pre.next
    #         b = a.next
    #         pre.next, a.next, b.next = b, b.next, a
    #         pre = a
    #     return dummy.next
