class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dic = {}

        for num in nums:
            if dic.get(num) == None:
                dic[num] = 1
            else:
                dic[num] += 1

        largest = 0
        num = 0
        for k, v in dic.items():
            if v > largest:
                num = k
                largest = v

        return num
            