class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return all(A[i]>=A[i+1] for i in range(0,len(A)-1)) or all(A[i]<=A[i+1] for i in range(0,len(A)-1))