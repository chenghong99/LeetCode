class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        l = 0
        r = x
        res = 0
        
        while l <= r:
            mid = l + ((r - l) // 2)
            if mid**2 > x:
                r = mid - 1
                
            elif mid**2 < x:
                l = mid + 1
                res = mid
            else:
                return mid
        return res
        