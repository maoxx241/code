class Solution:
    def countLetters(self, S: str) -> int:
        S = ' '+ S + ' '
        total, count = 0, 1
        for i in range(1, len(S)-1):
            if S[i] != S[i-1]:
                count = 1
            else:
                count += 1 
            total += count
        return total