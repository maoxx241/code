class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if min(m,n)==1:
            return 1
        table=[i for i in range(max(m,n)+1)]
        @lru_cache
        def helper(n1,n2):
            if n1 == 2:
                return table[n2]
            if n2 ==2 :
                return table[n1]
            
            return helper(n1-1,n2)+helper(n1,n2-1)
        
        return helper(m,n)
        
from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)