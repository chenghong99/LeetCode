class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ## prefix sum qn. curr sum = x, find number of curr_sum - k that occurs before curr 
        hashmap = {0:1} ## initialise with 0:1 for case where first item = k
        curr_sum = 0
        output = 0

        for i in nums:
            curr_sum += i ## get curr_sum at current position
            output += hashmap.get(curr_sum - k, 0) ## curr_sum - (curr_sum - k) = k
            hashmap[curr_sum] = hashmap.get(curr_sum, 0) + 1

        return output

        