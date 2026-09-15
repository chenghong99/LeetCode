class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## 1) populate hashmap with all values available 
        ## 2) iterate the list and find corresponding value 

        hashmap = {}

        for pos, num in enumerate(nums):
            lookup = target - num
            if lookup in hashmap:
                return [pos, hashmap.get(lookup)]
            hashmap[num] = pos
        return []