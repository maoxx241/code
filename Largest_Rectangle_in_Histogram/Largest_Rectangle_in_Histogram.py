class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        heights.append(0)
        stack=[-1]
        ans=0
        for i in range(len(heights)):
            while heights[i]< heights[stack[-1]]:
                h=heights[stack.pop()]
                w=i-1-stack[-1]
                ans=max(ans,h*w)
            stack.append(i)
        
        heights.pop()
        return ans