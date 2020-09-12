class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        pos = 0

        while pos < len(bits) - 1:
            if bits[pos] == 0:
                pos += 1
            else:
                pos += 2

        return pos != len(bits)