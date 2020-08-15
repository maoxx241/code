class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def helper(lst,depth):
            if depth>numRows:
                return 
            
            lst.append([0]*depth)
            for i in range(depth):
                if i == 0 or i ==depth-1:
                    lst[depth-1][i]=1
                    continue
                
                lst[depth-1][i]=lst[depth-2][i-1]+lst[depth-2][i]
            
            helper(lst,depth+1)
        
        res=[]
        helper(res,1)
        return res