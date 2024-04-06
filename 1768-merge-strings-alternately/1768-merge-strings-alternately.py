class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ls = ""
        
        while word1 and word2:
            ls += word1[0]
            ls += word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
            
        ls += word1
        ls += word2
        
        return ls
        