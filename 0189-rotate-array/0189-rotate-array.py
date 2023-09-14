class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        new_nums_front = []
        new_nums_back = []
        for i in range(len(nums) - k):
            new_nums_back.append(nums[i])
        for i in range(len(nums) - k, len(nums)):
            new_nums_front.append(nums[i])
        for i in range(k):
            nums[i] = new_nums_front[i]
        for i in range(k, len(nums)):
            nums[i] = new_nums_back[i - k]
        
