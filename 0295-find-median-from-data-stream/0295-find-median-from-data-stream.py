class MedianFinder:

    def __init__(self):
        self.list_left_max = []
        self.list_right_min = []
        
    def addNum(self, num: int) -> None:
        if len(self.list_left_max) == len(self.list_right_min):
            if len(self.list_left_max) == 0:
                heapq.heappush(self.list_left_max, -num)
            else:
                x = heapq.heappop(self.list_right_min)
                if x > num:
                    heapq.heappush(self.list_left_max, -num)
                    heapq.heappush(self.list_right_min, x)
                else:
                    heapq.heappush(self.list_left_max, -x)
                    heapq.heappush(self.list_right_min, num)
                
        else:
            x = heapq.heappop(self.list_left_max)
            x = -x
            if x > num:
                heapq.heappush(self.list_right_min, x)
                heapq.heappush(self.list_left_max, -num)
            else:
                heapq.heappush(self.list_right_min, num)
                heapq.heappush(self.list_left_max, -x)
        

    def findMedian(self) -> float:
        if len(self.list_left_max) == len(self.list_right_min):
            x = heapq.heappop(self.list_right_min)
            y = heapq.heappop(self.list_left_max)
            y = -y
            heapq.heappush(self.list_left_max, -y)
            heapq.heappush(self.list_right_min, x)
            return (x + y) / 2
        else:
            y = heapq.heappop(self.list_left_max)
            heapq.heappush(self.list_left_max, y)
            return -y
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()