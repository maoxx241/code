class Solution:
    def maximumSwap(self, num: int) -> int:
        A=[int(x) for x in str(num)]
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if d in last and last[d] > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num