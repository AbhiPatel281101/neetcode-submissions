class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        left, right = 0, len(heights) - 1

        while left < right:
            # Calculate the current area
            area = (right - left) * min(heights[left], heights[right])
            res = max(res, area)

            # Move the pointer pointing to the shorter line inward
            if heights[left] < heights[right]:
                left += 1 
            else:
                right -= 1
                
        return res