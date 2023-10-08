class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        dic = dict()
        ls = s.split(" ")
        hashset = set()
        if len(ls) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if dic.get(pattern[i]) == None:
                if ls[i] in hashset:
                    return False
                dic[pattern[i]] = ls[i]
                hashset.add(ls[i])
            elif dic.get(pattern[i]) != ls[i]:
                return False
        return True
            