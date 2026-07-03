class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_vol = 0
        for height in heights:
            width = r - l
            area = width * min(heights[l], heights[r])
            max_vol = max(max_vol, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return max_vol

            
