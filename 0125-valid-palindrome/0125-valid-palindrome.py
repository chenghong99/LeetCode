class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = [elem.lower() for elem in s if elem.isalnum()]
        rev_arr = arr[::-1]
        
        return arr == rev_arr
        
        
        
        