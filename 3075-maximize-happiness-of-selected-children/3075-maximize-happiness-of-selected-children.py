class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        heap = [-h for h in happiness]
        heapq.heapify(heap)
        counter = 0
        for i in range(k):
            temp = -heapq.heappop(heap)
            counter += max(temp - i, 0)
        return counter

        