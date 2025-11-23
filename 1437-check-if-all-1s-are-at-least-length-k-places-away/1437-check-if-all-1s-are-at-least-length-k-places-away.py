class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        ## just need to check the distance apart from the prev 1

        prev_pos = None

        for i, x in enumerate(nums):
            if prev_pos != None and x == 1:
                if i - prev_pos - 1 < k:
                    return False
                else:
                    prev_pos = i
            elif x == 1:
                prev_pos = i

        return True
        