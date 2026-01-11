class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p ## find this number or the smallest subset that sums to this number
        min_len = len(nums) ## start reducing this number using (pos - prefix_pos)

        if target == 0:
            return 0 

        prefix = {0:-1} ## initialise with 0:-1 base case 
        curr_sum = 0
        cum_sum = 0

        for pos, num in enumerate(nums):
            cum_sum += num
            curr_sum = cum_sum % p
            curr_target = (curr_sum - target + p) % p ## current target to look up in prefix
            if prefix.get(curr_target) != None:
                min_len = min(min_len, pos - prefix.get(curr_target)) ## update min len to remove 
            prefix[curr_sum] = pos ## update latest pos for prefix sum every iteration

        return -1 if min_len == len(nums) else min_len


        