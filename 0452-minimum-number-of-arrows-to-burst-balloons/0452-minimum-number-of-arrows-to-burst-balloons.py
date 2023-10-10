import sys 

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        ans = 1
        points.sort(key = lambda x : x[1])
        min_back = points[0][1]
        
        
        for i in range(len(points)):
            if points[i][0] > min_back:
                ans += 1
                min_back = points[i][1]

        return ans

        
                
        return ans
                
            
        