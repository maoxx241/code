class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         x, y = abs(a), abs(b)
#         # ensure that abs(a) >= abs(b)
#         if x < y:
#             return self.getSum(b, a)
        
#         # abs(a) >= abs(b) --> 
#         # a determines the sign
#         sign = 1 if a > 0 else -1
        
#         if a * b >= 0:
#             # sum of two positive integers x + y
#             # where x > y
#             while y:
#                 answer = x ^ y
#                 carry = (x & y) << 1
#                 x, y = answer, carry
#         else:
#             # difference of two integers x - y
#             # where x > y
#             while y:
#                 answer = x ^ y
#                 borrow = ((~x) & y) << 1
#                 x, y = answer, borrow
        
#         return x * sign
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)