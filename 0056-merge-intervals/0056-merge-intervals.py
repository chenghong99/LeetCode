class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x : (x[0], x[1]))
        final_list = [intervals[0]]

        for i in range(1, len(intervals)):
            if final_list[-1][0] <= intervals[i][0] <= final_list[-1][1]:
                last_item = final_list.pop()
                tail_val = max(last_item[1], intervals[i][1])
                final_list.append([last_item[0], tail_val])
            else:
                final_list.append([intervals[i][0], intervals[i][1]])

        return final_list

