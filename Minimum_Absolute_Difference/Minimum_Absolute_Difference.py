class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        m=float('inf')
        for i in range(1,len(arr)):
            m=min(m,arr[i]-arr[i-1])
        
        ans=[]
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==m:
                ans.append([arr[i-1],arr[i]])
        return ans