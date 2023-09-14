class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_vol = 0
        curr_vol = 0

        front = 0
        back = len(height) - 1

        while front != back:
            curr_vol = min(height[front], height[back]) * (back - front)
            max_vol = max(max_vol, curr_vol)
            if height[front] > height[back]:
                back -= 1
            else:
                front += 1

        return max_vol 
