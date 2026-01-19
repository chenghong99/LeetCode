class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ## populate eveything in hashmap, keep track of len of hashmap using a variable

        hashmap = {}
        hashset_tracker = set()
        for num in nums:
            if hashmap.get(num) == None:
                hashmap[num] = 1
                hashset_tracker.add(num)
            else:
                hashmap[num] += 1
                if num in hashset_tracker:
                    hashset_tracker.remove(num)

        output = 0

        for i in range(0, len(nums), 3):
            if len(hashmap) == len(hashset_tracker):
                return output
            output += 1
            for j in range(i, min(i + 3, len(nums) - 1)):
                hashmap[nums[j]] -= 1
                if hashmap[nums[j]] == 1:
                    hashset_tracker.add(nums[j])
                elif hashmap[nums[j]] == 0:
                    hashset_tracker.remove(nums[j])
                    hashmap.pop(nums[j])
        return output