class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        ## 2 maps -> first map to count all occurence of numberd 
        ## second map iterate and populate left num, first map - second map to get right numbers

        total_map = {}
        for num in nums:
            total_map[num] = total_map.get(num, 0) + 1 ## populate map with all num

        iter_map = {}
        output = 0
        MOD = 10**9 + 7
        for num in nums:
            target = num * 2
            if target in iter_map and target in total_map and total_map[target] - iter_map[target] > 0:
                left = iter_map[target]
                iter_map[num] = iter_map.get(num, 0) + 1
                output += (left * (total_map[target] - iter_map[target]))
            else:
                iter_map[num] = iter_map.get(num, 0) + 1

        return output % MOD

        