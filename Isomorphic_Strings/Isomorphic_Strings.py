class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
        if len(s) != len(t):
            return False
        for i,c in enumerate(s):
            if c not in dic:
                if t[i] not in dic.values():
                    dic[c]=t[i]
                else:
                    return False
            else:
                if t[i]!=dic[c]:
                    return False
        print(dic)
        return True