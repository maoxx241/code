class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c=max([can for can in candies])
        res=[]
        for can in candies:
            if can+extraCandies>=max_c:
                res.append(True)
            else:
                res.append(False)
        
        return res