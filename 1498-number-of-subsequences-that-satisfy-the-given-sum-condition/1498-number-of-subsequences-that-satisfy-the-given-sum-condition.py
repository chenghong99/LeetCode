class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ## sort list first then traverse 2 pointer sliding window 
        nums.sort() ## sort number on ascending order
        output = 0
        l, r = 0, len(nums) - 1
        mod = 10**9 + 7

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                output = (output + pow(2, r-l)) % mod
                l += 1
        return output 

