#https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        
        # Create a placeholder for each pile. In the worst case, the number of piles is the number of items in the list.
        topOfEachPile = [0] * len(nums)
        
        # From the deck/videos, we should know that  the Patience Algorithm is Greedy. This results in the fewest number of piles possible.
        # The LIS is then the number of piles that exist.
        # Here we create a variable that describes the number of piles that we have initialised from our placeholder above.
        numberOfPiles = 0
        
        # Iterate over each number. For each number, do binary search to figure out which of the piles to place the number.
        for n in nums:
            # These variables set the range of the binary search. We only want to do BS on the piles that have been initialised.
            # We include, at the very right, a new pile. This is useful because if the n can't fit into any of the existing piles we have to add it into this new pile.
            beg, end = 0, numberOfPiles
        
            # This BS is where we are greedy. If n is the same as l[middle] or less, we go left. 
            while beg != end:
                middle = (beg + end) // 2
                if n > topOfEachPile[middle]:
                    beg = middle + 1
                else:
                    end = middle
            
            # Update the top card at this pile.
            topOfEachPile[beg] = n
            
            # If we did end up using a new pile, then beg == numberOfPiles. 
            if beg == numberOfPiles: numberOfPiles += 1
        
        return numberOfPiles