class Solution:
    def countSubstrings(self, s: str) -> int:
        # res = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if s[i:j+1] == s[i:j+1][::-1]:
        #             res += 1
        # return res
        N = len(s)
        ans = 0
        for center in range(2*N - 1):
            left = center // 2
            right = left + center % 2

            while left >= 0 and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans