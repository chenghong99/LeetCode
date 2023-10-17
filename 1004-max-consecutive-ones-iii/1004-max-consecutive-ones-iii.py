class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        r = 0
        max_length = 0
        
        for i in range(len(nums)):
            while r < len(nums):
                if nums[r] == 1:
                    r += 1
                elif nums[r] == 0 and k == 0:
                    break
                else:
                    k -= 1
                    r += 1
                print(r)
                print(k)
            max_length = max(max_length, r - i)
            if nums[i] == 0:
                k += 1
        return max_length
                
            
            