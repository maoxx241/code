class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans=collections.Counter(A[0])
        for i in A:
            ans &= collections.Counter(i)
        return list(ans.elements())