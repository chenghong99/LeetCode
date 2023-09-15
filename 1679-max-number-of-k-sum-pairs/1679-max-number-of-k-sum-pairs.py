class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        dic = dict()
        hashset = set()
        ans = 0
        
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
            hashset.add(nums[i])
            
        for i in hashset:
            if k - i == i:
                mod = dic.get(i) // 2
                ans += mod
                dic[i] -= mod
            elif dic.get(k - i) != None and dic.get(i) != None:
                min_of_two = min(dic.get(k - i), dic.get(i))
                ans += min_of_two
                dic[k - i] -= min_of_two
                dic[i] -= min_of_two
                
        return ans