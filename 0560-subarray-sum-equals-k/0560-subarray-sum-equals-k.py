class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        dic = {0:1}
        curr_sum = 0
        ans = 0
        
        for i in nums:
            curr_sum += i
            if dic.get(curr_sum - k) != None:
                ans += dic.get(curr_sum - k)
                
            dic[curr_sum] = dic.get(curr_sum, 0) + 1
                
        return ans
                

        
## prefix sum 

        