class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_avg = 0
        curr_total = 0
        max_avg = -1000000000
        
        
        for i in nums[:k]:
            curr_total += i
        curr_avg = curr_total / k
        max_avg = max(max_avg, curr_avg)
        
        for i in range(k, len(nums)):
            curr_total -= nums[i - k]
            curr_total += nums[i]
            curr_avg = curr_total/k
            max_avg = max(max_avg, curr_avg)
            
            
        return max_avg
        