class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        
        new_list = []
        
        
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0] <= newInterval[1] or newInterval[0] <= intervals[i][1] <= newInterval[1]:
                if len(new_list) > 0:
                    if newInterval[0] <= new_list[-1][0] <= newInterval[1] or newInterval[0] <= new_list[-1][1] <= newInterval[1]:
                        new_list[-1][1] = max(intervals[i][1], newInterval[1])
                    else:
                        new_list.append([min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]) 
                else:
                    new_list.append([min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])])
            
            else:
                new_list.append(intervals[i])
                
        del intervals[:]
        
        for i in new_list:
            intervals.append(i)
        x = 0
        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[0] <= intervals[i][1] or intervals[i][0] <= newInterval[1] <= intervals[i][1]:
                x = 1
                break
        if x == 0:
            intervals.append(newInterval)
            intervals.sort()
            
        return intervals
                
        