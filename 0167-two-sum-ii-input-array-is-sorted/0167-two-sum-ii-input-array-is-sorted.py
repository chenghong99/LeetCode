class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        l , r = 0, len(numbers) - 1
        while r > l:
            if numbers[l] + numbers[r] == target:
                ans.append(l + 1)
                ans.append(r + 1)
                return ans
            
            elif numbers[l] + numbers[r] < target:
                l += 1
                
            else:
                r -= 1
        