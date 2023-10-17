class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        curr_max = max(candies)
        ans = []
        
        for i in candies:
            if i + extraCandies >= curr_max:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans
        