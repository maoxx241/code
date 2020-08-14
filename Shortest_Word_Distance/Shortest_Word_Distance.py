class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        dic={}
        for i,word in enumerate(words):
            if (word == word1 or word == word2) and word not in dic:
                dic[word]=[i]
            elif word == word1 or word ==word2:
                dic[word].append(i)
        
        sum=9999999
        for x in dic[word1]:
            for y in dic[word2]:
                sum=min(sum,abs(x-y))
        
        return sum