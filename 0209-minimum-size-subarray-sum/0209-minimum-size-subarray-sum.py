class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        if sum(nums) < target:
            return 0
        
        l = 0
        min_len = 10000000
        curr_sum = 0
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            
            while curr_sum >= target:
                min_len = min(min_len, r - l + 1)
                curr_sum -= nums[l]
                l += 1
                
        return min_len