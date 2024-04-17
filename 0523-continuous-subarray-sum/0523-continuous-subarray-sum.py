class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dic = {0 : -1}
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            mod = curr_sum % k
            
            if dic.get(mod) != None and i - dic.get(mod) > 1:
                return True
            elif dic.get(mod) == None:
                dic[mod] = i
                
        return False
 

## prefix sum 