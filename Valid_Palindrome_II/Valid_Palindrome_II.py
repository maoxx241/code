class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali_range(i, j):
            for k in range(i,j):
                if s[k]!=s[j-k+i]:
                    return False
            return True

        for i in range(len(s)//2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True
                    