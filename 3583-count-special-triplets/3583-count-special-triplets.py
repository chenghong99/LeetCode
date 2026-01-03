class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        ## iterate once and count all occurence of each number
        ## iterate one more time, at each iteration update a new dic and count the occurence 
        ## subtract from the first dic to get the number of occurence at the left 

        total_occurence = {}
        ans = 0
        MOD = 10**9 + 7

        for i in nums:
            total_occurence[i] = total_occurence.get(i, 0) + 1

        curr_occurence = {}
        for i in nums:
            target = i * 2
            left = curr_occurence.get(target, 0)
            curr_occurence[i] = curr_occurence.get(i, 0) + 1
            ans = (ans + left * (total_occurence.get(target, 0) - curr_occurence.get(target, 0))) % MOD
            

        return ans

