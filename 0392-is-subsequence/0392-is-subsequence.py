class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pos_of_s = 0
        
        if s == "":
            return True
        
        for i in range(len(t)):
            if s[pos_of_s] == t[i]:
                pos_of_s += 1
                if pos_of_s == len(s):
                    return True
        
        return False