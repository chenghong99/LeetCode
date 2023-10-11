class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        output = []
        
        if len(nums) == 0:
            return nums
        
        head = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                continue
            elif head == nums[i - 1]:
                output.append(str(head))
                head = nums[i]
            else:
                ans = str(head) + "->" + str(nums[i - 1])
                output.append(ans)
                head = nums[i]
        if head != nums[-1]:
            ans = str(head) + "->" + str(nums[-1])
            output.append(ans)
        else:
            output.append(str(head))
        return output
                