class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s_arr = [char for char in s if char.isalnum()]
        
        for i in range(len(s_arr) // 2):
            
            if s_arr[i] != s_arr[len(s_arr) - 1 - i]:
                return False
            
        return True
        
        
        
        