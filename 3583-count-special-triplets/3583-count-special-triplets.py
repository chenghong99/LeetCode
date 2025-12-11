import math
class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ## traverse from the right and keep track of the numbers visited in a dictionary.

        count = 0
        MOD = 10**9 + 7
        dic = {}
        traverse_dic = {}

        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        for j in nums:
            left = traverse_dic.get(j * 2, 0) 
            traverse_dic[j] = traverse_dic.get(j, 0) + 1
            right = dic.get(j * 2, 0) - traverse_dic.get(j * 2, 0)
            count = (count + right * left) % MOD

        return count

        