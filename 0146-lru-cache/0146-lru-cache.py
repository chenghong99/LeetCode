class LRUCache:

    def __init__(self, capacity: int):
        self.capcaity = capacity 
        self.cache = deque()
        self.dict = dict()
        

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.cache.remove(key)
        self.cache.appendleft(key)
        value = self.dict[key]
        return value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            if len(self.cache ) == self.capcaity:
                oldest = self.cache.pop()
                del self.dict[oldest]

                self.dict[key] = value
                self.cache.appendleft(key)
            else:
                self.dict[key] = value
                self.cache.appendleft(key)

        else: 
            self.cache.remove(key)   
            self.dict[key] = value
            self.cache.appendleft(key)
        
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)