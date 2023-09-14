class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        hashset = set()
        front = 0
        max_length = 0

        for back in range(len(s)):
            if s[back] not in hashset:
                hashset.add(s[back])
                max_length = max(max_length, len(hashset))
        
            else:
                while s[front] != s[back]:
                    hashset.remove(s[front])
                    front += 1
                front += 1
        
        return max_length 