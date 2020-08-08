class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for word in words:
            if word not in d:
                d[word]=1
            else:
                d[word]+=1
        d=sorted(sorted(d.items(), key = lambda x : x[0]), key = lambda x : x[1], reverse = True)  
        res=[]
        for i in range(k):
            res.append(d[i][0])
        return res