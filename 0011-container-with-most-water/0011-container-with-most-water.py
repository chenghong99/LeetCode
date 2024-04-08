class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head = 0 
        tail = len(height) - 1
        water = 0 
        
        while tail > head:
            curr_vol = min(height[head], height[tail]) * (tail - head)
            water = max(water, curr_vol)
            if height[tail] > height[head]:
                head += 1
            else:
                tail -= 1
        return water
        