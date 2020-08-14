class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split(' ')
        res=""
        for i in lst:
            res+=i[::-1]+" "
        return res[:-1]