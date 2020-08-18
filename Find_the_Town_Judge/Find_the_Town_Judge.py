class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
#         if not trust and N>1:
#             return -1
#         dic={}
#         s=(1+N)*N//2
#         for i in trust:
#             if i[0] not in dic:
#                 dic[i[0]]=[i[1]]
#                 s-=i[0]
#             else:
#                 dic[i[0]].append(i[1])
            
#         if s==0:
#             return -1
#         for i in dic:
#             if s not in dic[i]:
#                 return -1
#         return s
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1
        