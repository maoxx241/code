class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        j=len(A)-1
        ans=-1
        print(A)
        for i in range(len(A)):
            while A[i]+A[j]>=K and j>-1:
                j-=1
            if j<=i:
                break
            ans=max(ans,A[i]+A[j])
        
        return ans