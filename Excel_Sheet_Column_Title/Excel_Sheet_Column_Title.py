class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ''
        distance = ord('A') 

        while n > 0:
            y = (n-1) % 26
            n = (n-1) // 26
            s = chr(y+distance)
            result = ''.join((s, result))
            #result=s+result
        return result