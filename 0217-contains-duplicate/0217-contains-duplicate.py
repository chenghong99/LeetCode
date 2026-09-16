class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## set to store visited num
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False