class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d1=collections.Counter(arr1)
        ans=[]
        for n in arr2:
            ans+=[n]*d1[n]
            d1[n]-=d1[n]
        remain=[]
        for k in d1:
            remain+=[k]*d1[k]
        remain=sorted(remain)
        return ans+remain
        