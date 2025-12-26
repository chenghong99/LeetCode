class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """

        ## first sort the events by start time, then remove from smallest start time. at each start time continously iterate the pq to remove earlier events after each removal add the event to a pq. store the largest value before curr event. 

        prev_max_val = 0
        heap = [] ## empty heap to store prev events, 
        ## events consist of end time and value in [time, value] format 
        max_sum = 0

        events.sort(key = lambda x: x[0])
        for event in events:
            while heap and heap[0][0] < event[0]:
                temp_prev = heapq.heappop(heap)
                prev_max_val = max(prev_max_val, temp_prev[1])

            max_sum = max(max_sum, prev_max_val + event[2])
            heapq.heappush(heap, [event[1], event[2]])

        return max_sum



        