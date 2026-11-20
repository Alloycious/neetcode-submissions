class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Classic two pointer problem. To look for the max area,
        we start each pointer at the ends of the heights list. 
        This automatically assumes the widest length between both pointers. 
        
        We want to find the two max height from both ends with the furthest distance apart. Area = length * height = (r - j) * min(heights[l], heights[r]). Check this area against max area. If not greater in area, iterate the pointer that has the lower height.
        """
        l, r = 0, len(heights) - 1
        area = 0
        max_area = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(area, max_area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else: l += 1

        return max_area
