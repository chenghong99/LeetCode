class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## brute force, all iterations, 
        ## store min before curr pos, update min and max price 
        
        min_price = 1000000000000
        max_profit = 0

        for i in prices:
            min_price = min(i, min_price)
            max_profit = max(i - min_price, max_profit)

        return max_profit