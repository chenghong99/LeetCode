class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ## smallest pair with biggest, sort then 2 pointer front and back 
        nums.sort()
        min_max = 0
        for i in range(len(nums)//2):
            curr_pair = nums[i] + nums[len(nums) - i - 1]
            min_max = max(min_max, curr_pair)

        return min_max
        