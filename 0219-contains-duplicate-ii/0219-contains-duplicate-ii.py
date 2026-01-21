class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ## store the num in hashmap with their respective positions 
        hashmap = {} ## store latest num pos

        for pos, num in enumerate(nums):
            if hashmap.get(num) != None and pos - hashmap.get(num) <= k:
                return True 
            hashmap[num] = pos 
        return False