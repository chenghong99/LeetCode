class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ## insert and merge

        interval_len = len(intervals)
        for pos, interval in enumerate(intervals):
            if interval[0] > newInterval[0]:
                intervals.insert(pos, newInterval)
                break

        if interval_len == len(intervals):
            intervals.append(newInterval)

        new_interval = [intervals[0]]

        for i in range(1, len(intervals)):
            if new_interval[-1][1] >= intervals[i][0]:
                new_interval[-1][1] = max(intervals[i][1], new_interval[-1][1])
            else:
                new_interval.append(intervals[i])
        return new_interval