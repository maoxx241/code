class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dic={"1":"1","8":"8","6":"9","9":"6","0":"0"}
        left=0
        right=len(num)-1
        while left<=right:
            if num[left] not in dic or dic[num[left]]!=num[right]:
                return False
            left+=1
            right-=1
        
        return True