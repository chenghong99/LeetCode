class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ## sort by intervals start and merge with next interval 
        intervals.sort(key = lambda x : x[0])
        new_interval = [intervals[0]]

        for i in range(1, len(intervals)):
            if new_interval[-1][1] >= intervals[i][0]:
                new_interval[-1][1] = max(intervals[i][1], new_interval[-1][1])
            else:
                new_interval.append(intervals[i])
        return new_interval