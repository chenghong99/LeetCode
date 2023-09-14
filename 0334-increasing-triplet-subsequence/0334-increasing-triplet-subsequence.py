class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        left_min = []
        right_max = []
        curr_min = nums[0]
        curr_max = nums[-1]
        
        for i in range(len(nums)):
            curr_min = min(curr_min, nums[i])
            left_min.append(curr_min)
            
        for i in range(len(nums) - 1, -1, -1):
            curr_max = max(curr_max, nums[i])
            right_max.append(curr_max)
        right_max.reverse()
        
        for i in range(len(nums)):
            if left_min[i] < nums[i] and right_max[i] > nums[i]:
                return True
            
        return False