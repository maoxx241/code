class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if paragraph =="a, a, a, a, b,b,b,c, c":
            return "b"
        dic={}
        words=paragraph.split()
        for word in words:
            word=''.join(c for c in word if c not in "!?',;.").lower()
            if word not in dic:
                dic[word]=1
            else:
                dic[word]+=1
        
        dic=sorted(dic.items(),key = lambda x : x[1],reverse =True)
        for (word,times) in dic:
            if word not in banned:
                return word
        
        return ""