class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # isn't the theory behind 3rd solution just as simple as this:
        # a%k = x
        # b%k = x
        # (a - b) %k = x -x = 0
        # here a - b = the sum between i and j.
        # see above 4 line from bottom up, you'll see the math behind
        
        dic={}
        dic[0]=-1
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            if k!=0:
                sum %=k
            
            if sum in dic:
                if i - dic[sum]>1:
                    return True
            
            else:
                dic[sum]=i
        
        return False