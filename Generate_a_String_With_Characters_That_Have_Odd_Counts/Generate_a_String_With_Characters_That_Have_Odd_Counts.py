class Solution:
    def generateTheString(self, n: int) -> str:
        if n==1:
            return "a"
        return (n-2)*"a"+"b"+"c" if n % 2 else (n-1)*"a"+"b"