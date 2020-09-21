class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        tot = len(s)
        i, j = 0, 0
        
        while j < tot:
            while j < tot and s[j] != ' ':
                j += 1
            k = j - 1
            while i < k:  # reverse s[i:k+1]
                s[i], s[k] = s[k], s[i]
                i += 1
                k -= 1
            j += 1
            i = j