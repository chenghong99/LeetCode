class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap_num1 = []
        curr = res = 0
        ## Zip list ans sort by max of nums2
        new_list = sorted(zip(nums1, nums2), key=lambda x: -x[1]) 
        
        for a, b in new_list:
            curr += a
            heapq.heappush(heap_num1, a)
            
            if len(heap_num1) > k:
                curr -= heapq.heappop(heap_num1)
                
            if len(heap_num1) == k:
                res = max(res, curr * b)
                
        return res
        