class Solution:
    def splitArray(self, nums: List[int]) -> int:
        ## depends on where the split occurs, +- 1 index form that pos.
        ## get total sum first and each split get left array sum and right array sum

        curr_pos = 0
        increasing_sum = nums[curr_pos]
        max_split_pos = 0

        while curr_pos < len(nums) - 1:
            if nums[curr_pos] < nums[curr_pos + 1]:
                curr_pos += 1
                increasing_sum += nums[curr_pos]
            else:
                break

        max_split_pos = curr_pos
        if curr_pos < len(nums) - 1 and nums[max_split_pos] == nums[curr_pos + 1]:
            curr_pos += 1
        
        while curr_pos < len(nums) - 1:
            if nums[curr_pos] > nums[curr_pos + 1]:
                curr_pos += 1
            else:
                break

        if curr_pos != len(nums) - 1:
            return -1

        else:
            total_sum = sum(nums)
            first_case = abs((total_sum - increasing_sum) - increasing_sum)
            if max_split_pos < len(nums) - 1 and nums[max_split_pos] == nums[max_split_pos + 1]:
                return first_case
            increasing_sum -= nums[max_split_pos]
            second_case = abs((total_sum - increasing_sum) - increasing_sum)
            return min(first_case, second_case)