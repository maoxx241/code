class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) !=len(B):
            return False
        if not A:
            return True
        i=0
        while i <len(A):
            if A[i:]==B[0:len(A)-i]:
                if A[0:i]==B[len(A)-i:]:
                    return True
            i+=1
        return False
            