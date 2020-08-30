class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.dic=collections.defaultdict(list)
        ans=[]
        for lst in tickets:
            self.dic[lst[0]].append(lst[1])
        
        self.visitBitmap = {}
        
        for origin, lst in self.dic.items():
            lst.sort()
            self.visitBitmap[origin] = [False]*len(lst)
        
        self.flights = len(tickets)
        self.res=[]
        route = ['JFK']
        self.backtracking('JFK', route)
        return self.result
    
    def backtracking(self, origin, route):
        if len(route) == self.flights + 1:
            self.result = route
            return True

        for i, nextDest in enumerate(self.dic[origin]):
            if not self.visitBitmap[origin][i]:
                # mark the visit before the next recursion
                self.visitBitmap[origin][i] = True
                ret = self.backtracking(nextDest, route + [nextDest])
                self.visitBitmap[origin][i] = False
                if ret:
                    return True

        return False