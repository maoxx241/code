class Solution:
    def toGoatLatin(self, S: str) -> str:
        lst=S.split(' ')
        vowel={'a','e','i','o','u','A','E','I','O','U'}
        times=1
        for i in range(len(lst)):
            if lst[i][0] in vowel:
                lst[i]=lst[i]+'ma'+times*'a'
            else:
                lst[i]=lst[i][1:]+lst[i][0]+'ma'+times*'a'
            times+=1
        
        return ' '.join(lst)