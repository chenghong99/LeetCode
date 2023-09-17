class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        hm = {0:1}
        curr_sum = 0
        counter = 0

        for i in nums:
            curr_sum += i
            counter += hm.get(curr_sum - k, 0)
            hm[curr_sum] = hm.get(curr_sum, 0) + 1
        
        return counter
                