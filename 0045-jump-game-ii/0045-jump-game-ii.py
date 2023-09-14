class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        index = 0
        
        if len(nums) == 1:
            return 0
            
        while index + nums[index] < len(nums) - 1:
            max_distance = 0
            curr_distance = 0
            curr_index = 0
            for i in range(1, nums[index] + 1):
                curr_distance = index + i + nums[index + i]
                if max_distance < curr_distance:
                    max_distance = curr_distance
                    curr_index = i
            jumps += 1
            index += curr_index
        return jumps + 1
                
