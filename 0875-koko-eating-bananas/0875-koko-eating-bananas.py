import math 

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # cannot accept first h = count as ans as some other mid might be smaller 
        r = max(piles)
        l = 1
        temp = r
        
        while l <= r:
            mid = l + ((r - l) // 2)
            count = 0
            for i in piles:
                count += math.ceil(float(i) / mid)
                
            
            if count <= h:
                temp = mid
                r = mid - 1
                
            elif count > h:
                l = mid + 1
                
            
        return temp
            

