class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 : return False
        s=str(x)
        rs=s[::-1]
        return (False,True)[s==rs]
        
        