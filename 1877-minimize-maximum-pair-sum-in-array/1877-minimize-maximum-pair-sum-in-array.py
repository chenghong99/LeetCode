class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ## smallest pair with biggest, sort then 2 pointer front and back 
        nums.sort()
        min_max = 0
        for i in range(len(nums)//2):
            min_max = max(min_max, nums[i] + nums[-i - 1])

        return min_max
        