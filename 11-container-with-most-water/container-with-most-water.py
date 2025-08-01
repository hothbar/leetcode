class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        m = 0
        l, r = 0, n-1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            m = max(m, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return m