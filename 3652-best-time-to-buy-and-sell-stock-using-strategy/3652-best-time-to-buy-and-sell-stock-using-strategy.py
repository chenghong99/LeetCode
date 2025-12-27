class Solution(object):
    def maxProfit(self, prices, strategy, k):
        """
        :type prices: List[int]
        :type strategy: List[int]
        :type k: int
        :rtype: int
        """

        ## sliding window attempt, each window will be of length k. first k/2 will be hold next k/2 will be sell
        ## Action: at each window add first element back to hold. then sell new last element. 
        ## for example 2: second window, 4 - (4 + 3) + 5 = 8

        original = 0
        for i in range(len(strategy)):
            if strategy[i] == -1:
                original -= (prices[i])
            elif strategy[i] == 1:
                original += (prices[i])
        
        max_output = original
        curr_window = 0

        for i in range(k - 1, len(strategy)): ## element i will be the new element in the sliding window
            if i == k - 1:
                for j in range(k//2, k):
                   curr_window += prices[j]
                for x in range(k, len(strategy)):
                    if strategy[x] == -1:
                        curr_window -= (prices[x])
                    elif strategy[x] == 1:
                        curr_window += (prices[x])
            else:
                curr_window -= prices[i - (k // 2)]
                curr_window += prices[i]
                
                if strategy[i] == -1:
                    curr_window += (prices[i])
                elif strategy[i] == 1:
                    curr_window -= (prices[i])                                      
                if strategy[i - k] == -1:
                    curr_window -= (prices[i - k])
                elif strategy[i - k] == 1:
                    curr_window += (prices[i - k])
            max_output = max(max_output, curr_window)
        return max_output