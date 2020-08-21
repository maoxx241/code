class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         lst=[]
#         res=[]
#         for i in range(len(strs)):
#             d= collections.Counter(strs[i])
#             if d not in lst:
#                 lst.append(d)
#                 res.append([strs[i]])
#                 continue
#             for item in range(len(lst)):
#                 if lst[item]==d:
#                     res[item].append(strs[i])
        
#         return res
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()