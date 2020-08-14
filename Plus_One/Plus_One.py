class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index=-1
        cur=1
        while cur:
            cur, digits[index]= divmod(digits[index]+cur, 10)
            if cur ==0:
                break
            index-=1
            if index==-1-len(digits):
                return [1]+digits
        
        return digits
            