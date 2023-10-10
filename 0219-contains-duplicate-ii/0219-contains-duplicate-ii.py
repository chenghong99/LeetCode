class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        hm = dict()
        
        for i in range(len(nums)):
            if hm.get(nums[i]) == None:
                hm[nums[i]] = i
                
            elif i - hm.get(nums[i]) <= k:
                return True
            
            else:
                hm[nums[i]] = i
                
        return False
            