class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ## sort by start time, at each time continuously pop the pq until either the pq is empty or the remaining end time is larger than the current start time. add in current event. 

        events.sort(key = lambda x: x[0])
        heap = []
        prev_max, total_max = 0, 0

        for i in events:
            while heap and heap[0][0] < i[0]:
                temp = heapq.heappop(heap)
                prev_max = max(prev_max, temp[1])

            total_max = max(total_max, prev_max + i[2])
            heapq.heappush(heap,[i[1], i[2]])
        return total_max

        
