class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        current_price = prices[0]

        for price in prices:
            if current_price > price:
                current_price = price
            else:
                profit += (price - current_price)
                current_price = price

        return profit 