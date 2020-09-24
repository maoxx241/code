# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        ans=0
        for i in range(1,n):
            if knows(ans,i):
                ans=i
        
        if any(knows(ans, i) for i in range(ans)):
            return -1
        if any(not knows(i, ans) for i in range(n)):
            return -1
        return ans