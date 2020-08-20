class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        lst=str.split()
        if len(lst)!=len(pattern):
            return False
        dic={}
        for i,c in enumerate(pattern):
            if c not in dic:
                if lst[i] in dic.values():
                    return False
                dic[c]=lst[i]
            else:
                if lst[i]!=dic[c]:
                    return False
        
        return True
                
                
                
                
                
                
                