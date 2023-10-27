class RecentCounter:

    def __init__(self):
        self.de = deque()
        

    def ping(self, t: int) -> int:
        self.de.append(t)
        
        while self.de[0] < t - 3000:
            self.de.popleft()
            
        return len(self.de)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)