"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        temp=[]
        for s in schedule:
            for lst in s:
                    temp.append(lst)  
        temp=sorted((sorted(temp,key = lambda x: x.end)),key = lambda x: x.start )
        ans=[]
        cur=temp[0]
        for lst in temp:
            if lst.start>cur.end:
                ans.append(Interval(cur.end,lst.start))
                cur=lst
            else:
                if lst.end >cur.end:
                    cur.end=lst.end
        return ans