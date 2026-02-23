class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_water = 0
        
        while l < r:
            # Calculate current area
            width = r - l
            current_height = min(height[l], height[r])
            max_water = max(max_water, width * current_height)
            
            # Move the pointer of the shorter line
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_water
