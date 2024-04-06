class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        head = 0 
        tail = 0
        
        while tail < len(nums):
            if nums[tail] == 0:
                tail += 1
                
            else:
                nums[tail], nums[head] = nums[head], nums[tail]
                head += 1
                tail += 1
                
        return nums
        