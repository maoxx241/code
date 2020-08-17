class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        g=gcd(len(str1),len(str2))
        if g!=str2:
            index=0
            for i in range(0,len(str2)//g):
                if str2[0:g]!=str2[index:index+g]:
                    return ""
                index+=g
        index=0
        for i in range(0,len(str1)//g):
            if str2[0:g]!=str1[index:index+g]:
                return ""
            index+=g
        return str1[0:g]