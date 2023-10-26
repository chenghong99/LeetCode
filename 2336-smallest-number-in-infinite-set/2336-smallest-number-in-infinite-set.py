import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1,1001)]
        self.hash_set = set(range(1, 1001))
        
        

    def popSmallest(self) -> int:
        x = heapq.heappop(self.heap)
        self.hash_set.remove(x)
        return x
        
        

    def addBack(self, num: int) -> None:
        if num not in self.hash_set:
            self.hash_set.add(num)
            heapq.heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)