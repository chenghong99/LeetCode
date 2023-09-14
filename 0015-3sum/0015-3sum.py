class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        hashset = set()
        final_list = []

        for i, a in enumerate(nums):
            front = i + 1
            back = len(nums) - 1
            while front < back:
                combi = (a , nums[front], nums[back])
                combi_list = [a, nums[front], nums[back]]
                if nums[front] + a + nums[back] > 0:
                    back -= 1
                elif nums[front] + a + nums[back] < 0:
                    front += 1
                elif combi not in hashset:
                    hashset.add(combi)
                    final_list.append(combi_list)
                    back -= 1
                else:
                    back -= 1
        
        return final_list