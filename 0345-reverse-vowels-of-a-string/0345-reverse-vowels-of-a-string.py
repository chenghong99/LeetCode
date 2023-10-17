class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = [x for x in s]
        store = []
        
        for i in s:
            if i in ['a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U']:
                store.append(i)
                
        
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U']:
                s[i] = store[-1]
                store.pop(-1)
        str1 = ""
        return str1.join(s)
        