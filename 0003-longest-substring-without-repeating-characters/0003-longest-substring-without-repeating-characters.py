class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tail = 0 
        exist_set = set()
        max_len = 0
        
        for pos, char in enumerate(s):
            if char not in exist_set:
                exist_set.add(char)
                max_len = max(max_len,pos-tail+1)
            else:
                while s[tail] != char:
                    exist_set.remove(s[tail])
                    tail += 1
                tail += 1
        return max_len