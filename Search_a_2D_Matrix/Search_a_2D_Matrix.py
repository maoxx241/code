class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        i=len(matrix)-1
        j=0
        n=len(matrix)
        m=len(matrix[0])
        while 0<=i<n and 0<=j<m:
            if matrix[i][j]==target:
                return True
            
            if matrix[i][j]>target:
                i-=1
            else:
                j+=1
        
        return False