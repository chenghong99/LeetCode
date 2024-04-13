class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ans = []
        l, r = 0, len(numbers) - 1
        
        while l < r: 
            cur = numbers[l] + numbers[r]
            if cur == target:
                ans.append(l + 1)
                ans.append(r + 1)
                return ans 
            
            elif cur > target:
                r -= 1
                
            else:
                l += 1
        