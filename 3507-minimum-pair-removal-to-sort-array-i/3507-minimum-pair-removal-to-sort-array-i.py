class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ## brute force, iterate if not non decreasing get min sum and replace.
        operations = 0
        while True:
            non_decreasing = True
            small_pair_right_index = 0
            small_sum = 100000000
            
            for i in range(1, len(nums)):
                curr_sum = nums[i] + nums[i - 1]
                if curr_sum < small_sum:
                    small_pair_right_index = i
                    small_sum = curr_sum
                if nums[i] < nums[i - 1]:
                    non_decreasing = False
                    
            if non_decreasing == True:
                return operations

            nums[small_pair_right_index] = small_sum
            nums.pop(small_pair_right_index - 1)
            operations += 1
