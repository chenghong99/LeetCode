class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## hashset to store all the numbers, iterate the array and find consective numbers from hashset. store the head in hashmap and corresponding consecutive num. 
        
        hashset = set(nums)
        longest = 0
        curr_longest = 0
        
        for i in nums:
            if i - 1 not in hashset:
                curr_longest = 1
                while i + 1 in hashset:
                    curr_longest += 1
                    i += 1
                    
                longest = max(longest, curr_longest)
        return longest                