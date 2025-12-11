class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        ## create a dic with key, values -> key being the letter, and values being the occurence
        ## sort the values in descending order and concat into a string 

        dic = {}

        for i in s:
            dic[i] = dic.get(i, 0) + 1

        ans = ''
        for i in sorted(dic.items(), key = lambda x : x[1], reverse = True):
            ans += i[0] * i[1]

        return ans
        