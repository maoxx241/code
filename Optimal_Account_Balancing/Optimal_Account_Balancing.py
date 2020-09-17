class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # d, positive, negative=collections.defaultdict(int), [], []
        # #find the balance of every person and use to list to store the corresponding positive and negative balances.
        # #Ignore those with 0 balance.
        # for x, y, val in transactions:
        #     d[x]-=val
        #     d[y]+=val
        # for item in d.values():
        #     if item>0:
        #         positive.append(item)
        #     elif item<0:
        #         negative.append(item)
        # q=collections.deque([[positive, negative, 0]])
        # #BFS
        # while q:
        #     pos, neg, num=q.popleft()
        #     if not pos and not neg:
        #         return num
        #     #If we encounter a pair in pos and neg that sum to 0, it is guaranteed to have the 
        #     #minimum transaction in this step: eliminate them from pos and neg lists, we no longer 
        #     #need to conduct BFS at this step.
        #     if -pos[0] in neg: 
        #         index=neg.index(-pos[0])
        #         q.append([pos[1:], neg[:index]+neg[index+1:], num+1])
        #         continue
        #     #Conduct BFS if not
        #     for i in range(len(neg)):
        #         if pos[0]+neg[i]<0:
        #             q.append([pos[1:], neg[:i]+[pos[0]+neg[i]]+neg[i+1:], num+1])
        #         else:
        #             q.append([[pos[0]+neg[i]]+pos[1:], neg[:i]+neg[i+1:], num+1])
        # return 0
        tuplify = lambda balance: tuple(sorted((k, v) for k, v in balance.items()))

        @lru_cache(None)
        def dfs(balances):
            if not balances:
                return 0
            res = math.inf
            balances = {k: v for k, v in balances}
            for size in range(2, len(balances) + 1):
                for group in itertools.combinations(balances.keys(), size):
                    if sum(balances[k] for k in group) == 0:
                        remaining_balances = {k: v for k, v in balances.items() if k not in group}
                        res = min(res, size - 1 + dfs(tuplify(remaining_balances)))
            return res

        balances = collections.defaultdict(int)
        for u, v, z in transactions:
            balances[u] += z
            balances[v] -= z
        return dfs(tuplify({k: v for k, v in balances.items() if v}))