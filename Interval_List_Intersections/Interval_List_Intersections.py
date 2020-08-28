class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        ans=[]
        while i<len(A) and j<len(B):
            if A[i][1]<B[j][0]:
                i+=1
                continue
                
            if B[j][1]<A[i][0]:
                j+=1
                continue
            
            lst=[max(A[i][0],B[j][0]),min(A[i][1],B[j][1])]
            ans.append(lst)
            if A[i][1]>B[j][1]:
                j+=1
            else:
                i+=1
        
        return ans
                
                