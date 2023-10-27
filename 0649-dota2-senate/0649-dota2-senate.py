class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue_r = deque()
        queue_d = deque()
        n = len(senate)
        
        for i in range(len(senate)):
            if senate[i] == "R":
                queue_r.append(i)
            else:
                queue_d.append(i)
                
        while queue_r and queue_d:
            r_pop = queue_r.popleft()
            d_pop = queue_d.popleft()
            if r_pop > d_pop:
                queue_d.append(n + d_pop)
            else:
                queue_r.append(n + r_pop)
                
        return "Radiant" if queue_r else "Dire"
                
        