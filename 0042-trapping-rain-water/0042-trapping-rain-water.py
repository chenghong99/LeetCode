class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_ls = []
        right_ls = []
        right_max = 0
        left_max = 0
        vol = 0

        for i in range(len(height)):
            left_ls.append(left_max)
            left_max = max(left_max, height[i])
        
        for i in range(len(height) - 1, -1, -1):
            right_ls.append(right_max)
            right_max = max(right_max, height[i])
        right_ls.reverse()

        for i in range(len(height)):
            left_right_min = min(right_ls[i], left_ls[i])
            vol += max((left_right_min - height[i]), 0)

        return vol
        
