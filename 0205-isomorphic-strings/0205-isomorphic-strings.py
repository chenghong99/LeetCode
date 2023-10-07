class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dic = dict()
        s_set = set()
        ls_s = list(s)
        ls_t = list(t)
        
        for i in range(len(s)):
            if dic.get(t[i]) == None:
                if s[i] in s_set:
                    return False
                s_set.add(s[i])
                dic[t[i]] = s[i]
                ls_t[i] = ls_s[i]
            else:
                ls_t[i] = dic.get(t[i])
        return ls_s == ls_t
                
                
            
            
        
                 
        
            
        