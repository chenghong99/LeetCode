class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        prefix_sum = {0:1}
        total = 0
        
        for i in nums:
            curr_sum += i
            total += prefix_sum.get(curr_sum - k, 0)
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
            
            
        return total
                 
        