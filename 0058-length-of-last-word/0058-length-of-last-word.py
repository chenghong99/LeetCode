class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s[::-1]
        index  = 0
        
        while s[index] == " ":
            index += 1
            
        for i in range(index,len(s)):
            if s[i] == " ":
                return i - index
            
        return len(s) - index
        