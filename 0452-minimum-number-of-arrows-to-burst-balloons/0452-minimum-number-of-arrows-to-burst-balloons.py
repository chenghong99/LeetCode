class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ## sort by start, find overlap and non overlap region and determine how many balloons to shoot 
        points.sort(key = lambda x: x[1])
        output = 0
        prev = -10000000000000000

        for start, end in points:
            if start > prev:
                output += 1
                prev = end 
        return output 
