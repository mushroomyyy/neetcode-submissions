class Solution:
    def trap(self, height: List[int]) -> int:
        max_vol = 0
        l = 0
        r = len(height) - 1
        l_max, r_max = 0,0

        while l < r:
            if height[l] < height[r]:
                l_max = max(l_max,height[l])
                max_vol += l_max - height[l]
                l += 1
            else:
                r_max = max(r_max,height[r])
                max_vol += r_max - height[r]
                r -= 1
        return max_vol


        