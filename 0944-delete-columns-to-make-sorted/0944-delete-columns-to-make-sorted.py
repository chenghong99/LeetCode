class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        ## time complexity will be O(n2) for sure as i will need to iterate all strings, where n is the length of a single string 
        counter = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j][i] > strs[j + 1][i]:
                    counter += 1
                    break
        return counter

        