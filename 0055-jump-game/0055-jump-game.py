class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_max = 0
        
        for pos, val in enumerate(nums):
            curr_max = max(curr_max, pos + val)
            if curr_max == len(nums) - 1:
                return True
            if curr_max == pos:
                return False
            
        return True 
    