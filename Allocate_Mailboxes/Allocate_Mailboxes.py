class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
            #  sort the houses, cause we dont want to have a situation where houses [301, 240, 360] 
        houses.sort()

        #  Memo table, using a dictionary is easier but slower
        memo = [[[-1 for i in range(len(houses) + 3)] for j in range(len(houses) + 3)] for _ in range(k + 3)]

        #  left = left index of sorted houses, right = Including right index, num = num of mailbox that we can place for this group
        def helper(left, right, num):

            #  previously computed, lets not waste time to compute it again
            if memo[num][left][right] != -1:
                return memo[num][left][right]

            #  too many mailbox, too little houses, we have done something wrong in grouping earlier grouping. So return a 'FAIL' answer
            if right - left  + 1 < num:
                return float('inf')

            #  Base case, one mailbox, put mailbox in median of houses. 
            if num == 1:
                ans = 0
                mid = (left + right) // 2
                for i in range(left, right + 1):
                    ans += abs(houses[i] - houses[mid])
                memo[num][left][right] = ans
                return ans

            #  Have a mailbox for every house, great!
            if num == right - left + 1:
                return 0


            ans = float('inf')

            #  "Careful Brute Force"
            for i in range(left, right):
                ans = min(ans, helper(left, i, 1) + helper(i + 1, right, num - 1))

            #  Store ans
            memo[num][left][right] = ans
            return ans


        return helper(0, len(houses) - 1, k)
