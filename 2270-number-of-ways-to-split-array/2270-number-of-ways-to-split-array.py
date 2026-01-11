class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ## get total sum first, with each iteration total_sum - iter_sum 
        total_sum = sum(nums)
        split = 0
        iter_sum = 0

        for i in nums[:-1]:
            iter_sum += i
            if total_sum - iter_sum <= iter_sum:
                split += 1
        return split


        