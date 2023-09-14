class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                max_profit = max(max_profit, (prices[right] - prices[left]))
            right += 1

        return max_profit
