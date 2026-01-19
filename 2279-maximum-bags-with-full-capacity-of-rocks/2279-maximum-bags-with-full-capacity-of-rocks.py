class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        ## find the difference, between capacity and number of rocks, and sort 
        diff = []

        for i in range(len(capacity)):
            rock_diff = capacity[i] - rocks[i]
            diff.append(rock_diff)

        diff.sort(reverse = True)
        print(diff)
        output = 0

        while additionalRocks > 0:
            if diff and additionalRocks - diff[-1] >= 0:
                additionalRocks -= diff[-1]
                output += 1
                diff.pop()
            else:
                break

        return output