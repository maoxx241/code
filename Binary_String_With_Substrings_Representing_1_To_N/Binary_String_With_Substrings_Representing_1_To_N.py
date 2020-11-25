class Solution:
    def queryString(self, S: str, N: int) -> bool:
        m = N // 2
		# You only need to check half of the range.
		# each of the first half is the subset of the second
        for i in range(m + 1, N + 1):
            if not bin(i)[2:] in S:
                return False
        return True