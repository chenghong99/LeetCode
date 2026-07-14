class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        interim_pos = 1
        prev = nums[0]

        for pos, num in enumerate(nums[1:], start=1):
            if nums[pos] != prev:
                nums[pos], nums[interim_pos] = nums[interim_pos], nums[pos]
                interim_pos += 1
                prev = num
        return interim_pos



