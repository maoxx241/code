class Solution:
    # def fib(self, N: int) -> int:
    #     if N==0:
    #         return 0
    #     if N==1:
    #         return 1
    #     return self.fib(N-1)+self.fib(N-2)
    def fib(self, N: int) -> int:
        a = []
        a.append(0)
        a.append(1)
        for i in range(2, 31):
            tmp = a[i-1] + a[i-2]
            a.append(tmp)
        return a[N]
            