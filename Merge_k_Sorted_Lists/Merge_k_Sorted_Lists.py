# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#https://en.wikipedia.org/wiki/Priority_queue
#https://docs.python.org/3/library/queue.html
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        q = PriorityQueue(maxsize=k)
        dummy = ListNode(None)
        curr = dummy
        for list_idx, node in enumerate(lists):
            if node: q.put((node.val, list_idx, node))
        while q.qsize() > 0:
            poped = q.get()
            curr.next, list_idx = poped[2], poped[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, list_idx, curr.next))
        return dummy.next
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lst=[]
        for i in range(len(lists)):
            while lists[i]!=None:
                lst.append(lists[i].val)
                lists[i]=lists[i].next
        if not lst:
            return None
        lst.sort()
        ans=temp=ListNode(lst[0])
        for i in range(1,len(lst)):
            temp.next=ListNode(lst[i])
            temp=temp.next
        return ans

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next