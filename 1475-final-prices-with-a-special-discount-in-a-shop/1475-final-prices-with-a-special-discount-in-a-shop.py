class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """

        stack = []

        for i, p in enumerate(prices):
            while len(stack) != 0 and prices[stack[-1]] >= p:
                prices[stack.pop()] -= p
            stack.append(i)

        return prices
                