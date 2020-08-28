class Solution:
    def hammingWeight(self, n: int) -> int:
        # ans=0
        # for c in bin(n):
        #     if c=='1':
        #         ans+=1
        # return ans
        bits=0
        mask=1
        for i in range(32):
            if n & mask !=0:
                bits+=1
            mask<<=1
        
        return bits
