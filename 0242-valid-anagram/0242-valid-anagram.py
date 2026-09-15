class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ## sort both and match O(nlogn)
        ## hashmap to count O(n)

        if len(t) != len(s):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        return s_count == t_count