class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic={}
        for item in items:
            if item[0] not in dic:
                dic[item[0]]=[item[1]]
            else:
                dic[item[0]].append(item[1])
        
        res=[]
        for i in dic:
            lst=sorted(dic[i],reverse=True)[:5]
            res.append([i,sum(lst)//len(lst)])
        return res