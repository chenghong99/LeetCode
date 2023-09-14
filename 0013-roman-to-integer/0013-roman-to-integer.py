class Solution(object):
    def romanToInt(self, s):
        num = 0
        dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

        for i in range(len(s) - 1):
            if dic[s[i]] < dic[s[i + 1]]:
                num -= dic[s[i]]
            else:
                num += dic[s[i]]
        return num + dic[s[-1]]
