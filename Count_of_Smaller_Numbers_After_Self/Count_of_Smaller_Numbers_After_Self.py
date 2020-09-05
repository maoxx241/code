class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def divide(tupn):
            if len(tupn) == 1:
                return tupn
            mid = len(tupn) // 2
            left = divide(tupn[:mid])
            right = divide(tupn[mid:])
            return conquer(left, right)
        
        def conquer(left, right):
            sor = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    sor.append(left[i])
                    res[left[i][1]] += len(right) - j
                    i += 1
                else:
                    sor.append(right[j])
                    j += 1
            sor.extend(left[i:] or right[j:])
            return sor
        
        if not nums:
            return []
        res = [0] * len(nums)
        tupn = [(n,i) for i,n in enumerate(nums)]

        divide(tupn)
        return res
        