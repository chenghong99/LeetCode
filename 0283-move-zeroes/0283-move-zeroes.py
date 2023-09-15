class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        pos_of_zero = 0
        
        for i in range(len(nums)):            
            if nums[i] != 0:
                nums[pos_of_zero], nums[i] = nums[i], nums[pos_of_zero]
                pos_of_zero += 1