class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        ## target for this mod = total_sum % 6 removing the smallest subarray that makes this mod is the ans 
        target = sum(nums) % p

        if target == 0:
            return 0

        mod_map = {0:-1} ## store prefix sum of mod map 
        curr_sum = 0
        small_len = len(nums)

        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % p ## current modulo
            to_find = (curr_sum - target + p) % p ## number to find 
            if to_find in mod_map:
                small_len = min(small_len, i - mod_map[to_find])
            mod_map[curr_sum] = i

        return -1 if small_len == len(nums) else small_len

