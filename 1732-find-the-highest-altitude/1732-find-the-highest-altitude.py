class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_al = 0
        curr_al = 0
        for i in gain:
            curr_al += i
            max_al = max(max_al, curr_al)
            
        return max_al
            
        