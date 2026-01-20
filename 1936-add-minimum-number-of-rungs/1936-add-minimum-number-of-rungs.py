class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        to_add = 0
        curr_height = 0

        for i in rungs:
            distance = i - curr_height
            if distance <= dist:
                curr_height = i 
            else:
                to_add = to_add + (distance // dist)
                if distance % dist == 0:
                    to_add -= 1
                curr_height = i
        return to_add
