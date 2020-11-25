class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        count1=collections.Counter(s1)
        
        if len(s2)==len(s1):
            return True if count1==collections.Counter(s2) else False
        count2=collections.Counter(s2[:len(s1)])
        for i,c in enumerate(s2[len(s1):]):
            if count2==count1:
                return True
            count2[s2[i]]-=1
            if count2[s2[i]]==0:
                del count2[s2[i]]
            count2[c]+=1
        
        return True if count1==count2 else False