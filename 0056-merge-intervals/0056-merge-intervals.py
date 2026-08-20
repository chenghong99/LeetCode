class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        new_interval = []
        intervals.sort(key=lambda x: x[0])
        
        for i in intervals:
            if len(new_interval) == 0:
                new_interval.append(i)
            elif new_interval[-1][0] <= i[0] <= new_interval[-1][1]:
                new_interval[-1][1] = max(i[1], new_interval[-1][1])
            else:
                new_interval.append(i)
        return new_interval