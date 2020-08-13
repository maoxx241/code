class Solution:
    def compress(self, chars: List[str]) -> int:
        anchor = write = 0
        for i, c in enumerate(chars):
            if i + 1 == len(chars) or chars[i + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if i > anchor:
                    for digit in str(i - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = i + 1
                
        return write