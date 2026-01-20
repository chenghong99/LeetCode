class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ## idea: sort first in descending order, order from large to small at the back to reduce number of negatives
        nums.sort(key = lambda x : -x)
        curr_sum = 0
        pos_count = 0

        for i in nums:
            curr_sum += i
            if curr_sum > 0:
                pos_count += 1
        return pos_count