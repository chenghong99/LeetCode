class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        hashset = set()
        ans = []
        
        for i in range(len(nums)):
            l , r = i + 1, len(nums) - 1
            
            while l < r:
                curr = [nums[i], nums[l], nums[r]]
                curr.sort()
                temp = tuple(curr)
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0 and temp not in hashset:
                    ans.append(curr)
                    hashset.add(temp)
                    l += 1
                    
                elif curr_sum > 0:
                    r -= 1
                    
                else:
                    l += 1
                    
        return ans
                    
                    