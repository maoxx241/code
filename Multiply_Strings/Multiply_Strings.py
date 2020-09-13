class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ""

        n1 = [int(x)*(10**(i)) for i, x in enumerate(reversed(num1))]
        n2 = [int(x)*(10**(i)) for i, x in enumerate(reversed(num2))]
        result = str(sum([x*y for x in n1 for y in n2]))

        return result

        