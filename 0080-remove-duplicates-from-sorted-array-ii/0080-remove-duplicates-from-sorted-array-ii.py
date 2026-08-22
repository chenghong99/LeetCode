class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## prev flag to track the preve elem. and dup boolean 
        ## keep track of 2 dups present. Compare with flag and boolean 
        ## replace_pos 

        prev_flag = nums[0]
        dup_bool = False
        replace_pos = 1

        for pos, num in enumerate(nums[1:]):
            if num != prev_flag:
                dup_bool = False
                nums[replace_pos] = num
                replace_pos += 1
                prev_flag = num
            elif num == prev_flag and dup_bool == False:
                dup_bool = True
                nums[replace_pos] = num
                replace_pos += 1
        return replace_pos 