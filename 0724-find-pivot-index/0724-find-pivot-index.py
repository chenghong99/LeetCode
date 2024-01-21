class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_count = 0
        left_count = 0
        for i in range(1, len(nums)):
            right_count += nums[i]
        
        if right_count == left_count:
            return 0
            
        for i in range(1, len(nums)):
            left_count += nums[i - 1]
            right_count -= nums[i]
            if right_count == left_count:
                return i
        return -1
            