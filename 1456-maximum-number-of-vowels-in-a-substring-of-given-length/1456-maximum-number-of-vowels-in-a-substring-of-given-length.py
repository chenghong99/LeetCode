class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = 0
        max_num = 0
        val = min(k, len(s))
        for i in range(val):
            if s[i] in ['a','e','i','o','u']:
                count += 1
                max_num = max(max_num, count)
                
        
        for i in range(k, len(s)):
            if s[i - k] in ['a','e','i','o','u']:
                count -= 1
                
            if s[i] in ['a','e','i','o','u']:
                count += 1
                
            max_num = max(max_num, count)
            
        return max_num
            
            
        