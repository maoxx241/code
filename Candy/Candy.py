class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        ans=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                ans[i]=ans[i-1]+1
        
        s=ans[-1]
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                ans[i]=max(ans[i],ans[i+1]+1)
            
            s+=ans[i]
        
        return s