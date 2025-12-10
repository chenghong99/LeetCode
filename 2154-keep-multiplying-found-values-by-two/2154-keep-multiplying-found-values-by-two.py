class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        hashtable = set(nums)

        while True:
            if original in hashtable:
                original *= 2
            else:
                return original 
        