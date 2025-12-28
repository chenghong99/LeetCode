class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ## for O(n + m) solution we note that at each strategic corner top right or bottom left we only need to traverse in a certain direction. bottom left up traverse up and right as we move to the first row. 

        starting_pos = -1
        for i, x in enumerate(grid[-1]):
            if x < 0:
                starting_pos = i
                break

        if starting_pos == -1:
            return 0
        else:
            col = starting_pos
            counter = len(grid[0]) - col
            for i in range(len(grid)-2,-1,-1):
                while col < len(grid[0]) - 1 and grid[i][col] >= 0:
                    col += 1                    
                if grid[i][col] >= 0 and col == len(grid[0]) - 1:
                    break
                counter += len(grid[0]) - col

            return counter
                