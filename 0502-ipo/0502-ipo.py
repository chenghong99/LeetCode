import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        
        min_heap_capital = []
        max_heap_profits = []
        money = 0
        perm = w
        
        for i in range(len(capital)):
            heapq.heappush(min_heap_capital, (capital[i], profits[i]))
            
        for i in range(k):
            while len(min_heap_capital) > 0:
                x = heapq.heappop(min_heap_capital)
                if x[0] <= w:
                    heapq.heappush(max_heap_profits, (-x[1], x[0]))
                else:
                    heapq.heappush(min_heap_capital, x)
                    break
            if len(max_heap_profits) != 0:
                max_cap = heapq.heappop(max_heap_profits)
                w += (-max_cap[0])
                money += (-max_cap[0])
            
        return money + perm