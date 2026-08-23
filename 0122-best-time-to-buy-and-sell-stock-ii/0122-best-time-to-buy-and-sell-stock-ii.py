class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for pos, num in enumerate(prices[:-1]):
            if num < prices[pos + 1]:
                profit += prices[pos + 1] - num
        return profit


