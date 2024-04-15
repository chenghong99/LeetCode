class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s[::-1]
        pos = 0
        count = 0
        
        while s[pos] == " ":
            pos += 1
                
        while pos < len(s) and s[pos] != " ":
            pos += 1
            count += 1
            
        return count 
        