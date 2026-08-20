class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ## switch with prev 

        moving_head = 0 
        for i, num in enumerate(nums):
            if num == 0:
                continue 
            else:
                nums[i], nums[moving_head] = nums[moving_head], nums[i]
                moving_head += 1
        return nums
        