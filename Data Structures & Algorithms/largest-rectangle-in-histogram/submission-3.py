class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        i = 0

        currWidth = 1
        currHeight = heights[i]
        
        for j in range(len(heights)):
            i = j
            right = j
            left = j
            currWidth = 1

            # Extend right
            while i < (len(heights) - 1) and heights[i + 1] >= heights[j]:
                currWidth += 1
                i += 1
            right = i
            i = j

            print(f"right: ", right)
            # Extend left
            while i > 0 and heights[i - 1] >= heights[j]:
                currWidth += 1
                i -= 1
            left = i

            print(f"left: ", left)
            print(f"currWidth: ", currWidth)
            area = heights[j] * currWidth
            maxArea = max(area, maxArea)
            print(f"maxArea: ", maxArea)
            
        
        return maxArea
            




