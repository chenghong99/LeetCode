class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        t_dic = {}
        window_dic = {}

        for char in t:
            t_dic[char] = t_dic.get(char, 0) + 1

        res = [-1, -1]
        res_len = 1000000000
        l = 0
        have = 0
        need = len(set(t))

        for r in range(len(s)):
            window_dic[s[r]] = window_dic.get(s[r], 0) + 1

            if t_dic.get(s[r]) != None:
                if window_dic[s[r]] == t_dic[s[r]]:
                    have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)

                window_dic[s[l]] -= 1

                if t_dic.get(s[l]) != None:
                    if t_dic.get(s[l]) > window_dic[s[l]]:
                        have -= 1
                l += 1

        l, r = res
        if res_len == 1000000000:
            return ""
        else:
            return s[l:r+1]
                

