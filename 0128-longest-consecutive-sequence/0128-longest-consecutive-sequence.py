class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## store all in dic 
        ## find the head and iterate till tail while popping each elem 

        num_set = set(num for num in nums)
        max_len = 0
        
        for num in nums:
            if num - 1 not in num_set:
                curr_len = 0
                while num in num_set:
                    curr_len += 1
                    num_set.remove(num)
                    num += 1
                max_len = max(max_len, curr_len)
        return max_len