class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        curr = 1
        prev = nums[0]

        for num in nums:
            if num == prev:
                continue 
            else:
                nums[curr] = num
                prev = num
                curr += 1
        return curr