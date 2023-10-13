import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        
        
        for i in nums:
            heapq.heappush(heap, -i)
            
        ans = 0
        for i in range(k):
            ans = heapq.heappop(heap)
            
        return ans * -1
            
        