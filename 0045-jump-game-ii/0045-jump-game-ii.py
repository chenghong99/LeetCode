class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## at each point, iterate the full numebr of steps, at each point of the step project the max 

        curr_pos = 0 ## for while loop pos
        next_pos = 0 ## projected next pos
        max_projection = 0 ## project next max step
        num_steps = 0 ## final output

        while curr_pos < len(nums) - 1:
            if curr_pos + nums[curr_pos] >= len(nums) - 1:
                return num_steps + 1
            for step in range(1, nums[curr_pos] + 1):
                if nums[curr_pos + step] + curr_pos + step > max_projection:
                    max_projection = nums[curr_pos + step] + curr_pos + step
                    next_pos = curr_pos + step
            max_projection = 0
            curr_pos = next_pos
            num_steps += 1
        return num_steps
