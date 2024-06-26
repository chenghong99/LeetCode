# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        low = 1
        high = n
        mid = None 
        ans = 0
        
        while low <= high:
            mid = low + ((high - low) // 2)
            if isBadVersion(mid):
                ans = mid
                high = mid - 1
                
            else:
                low = mid + 1
                
        return ans
            