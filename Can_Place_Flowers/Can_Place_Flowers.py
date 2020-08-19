class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        nn=0
        i=0
        while i<len(flowerbed):
            if flowerbed[i]==1:
                i+=2
            elif (i ==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                nn+=1
                if nn==n:
                    return True
                i+=2
            else:
                i+=1
        
        return False