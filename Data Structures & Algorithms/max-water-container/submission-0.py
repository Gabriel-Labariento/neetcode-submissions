class Solution:
    def maxArea(self, heights: List[int]) -> int:
        am = {}

        l, r = 0, len(heights) - 1

        while l < r:
            greater = r if heights[r] >= heights[l] else l
            smaller = l if heights[l] <= heights[r] else r
            am[(l, r)] = heights[smaller] * abs(greater - smaller)

            # Change what's smaller
            if l == smaller:
                l += 1
            else:
                r -= 1
            
        maxArea = -1
        for k, v in am.items():
            if v > maxArea:
                maxArea = v
        
        print(am)
        return maxArea

