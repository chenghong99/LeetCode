class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = nums[0]
        curr_max = nums[0]

        for i in nums[1:]:
            curr_max = max(curr_max + i, i)
            ans = max(curr_max, ans)

        return ans

        