class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not n :
            return len(tasks)
        dic=collections.Counter(tasks)
        lst=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        count=0
        for i in range(len(lst)):
            if lst[i][1]==lst[0][1]:
                count+=1
            else:
                break
        return max((n+1)*(lst[0][1]-1)+count,len(tasks))