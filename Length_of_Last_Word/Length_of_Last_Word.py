class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        lst=s.split(' ')
        for i in reversed(lst):
            if i:
                return len(i)
            
        return 0