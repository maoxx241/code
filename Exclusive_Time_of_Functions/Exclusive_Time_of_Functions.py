class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans=[0]*n
        stack=[]
        prev_time=0
        for log in logs:
            fun,state,time=log.split(':')
            fun,time=int(fun),int(time)
            
            if state=='start':
                if stack:
                    ans[stack[-1]]+=time-prev_time
                stack.append(fun)
                prev_time=time
            else:
                ans[stack.pop()]+=time-prev_time+1
                prev_time=time+1
        
        return ans