class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
#         if rowIndex==0:
#             return [1]
#         if rowIndex==1:
#             return [1,1]
        
#         def helper(base,i):
#             if i == rowIndex+1:
#                 return base
#             lst=[1]*(i+1)
#             for j in range(1,len(lst)-1):
#                 lst[j]=base[j-1]+base[j]
#             return helper(lst,i+1)
        
#         return helper([1,1],2)
        ans=[1]
        for i in range(1,rowIndex+1):
            ans.append(ans[-1]*(rowIndex-i+1)//i)
        return ans