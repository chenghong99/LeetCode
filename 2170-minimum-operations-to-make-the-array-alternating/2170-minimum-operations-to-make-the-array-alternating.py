class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ## count the frequency of each element in the odd and even position 
        ## the max alternating combo will be the highest freq odd and even number, count the number of non max highest freq. 

        odd_indices = {}
        even_indices = {}
        odd_flag = True

        if len(nums) == 1:
            return 0

        for num in nums:
            if odd_flag:
                odd_indices[num] = odd_indices.get(num, 0) + 1
                odd_flag = False
            else:
                even_indices[num] = even_indices.get(num, 0) + 1
                odd_flag = True

        sorted_odd = sorted(odd_indices.items(), key = lambda x: x[1], reverse = True)
        sorted_even = sorted(even_indices.items(), key = lambda x: x[1], reverse = True)
        sorted_even.append((0, 0))
        sorted_odd.append((0, 0))

        if sorted_odd[0][0] == sorted_even[0][0]:
            return min(len(nums) - sorted_odd[0][1] - sorted_even[1][1], len(nums) - sorted_odd[1][1] - sorted_even[0][1])
        else:
            return len(nums) - sorted_odd[0][1] - sorted_even[0][1]


        
