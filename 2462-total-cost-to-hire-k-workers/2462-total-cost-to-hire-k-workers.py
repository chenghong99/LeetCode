class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        front_pq = costs[:candidates]
        rear_pq = costs[max(candidates, len(costs) - candidates):]
        ans = 0
        head_ref = candidates
        tail_ref =  len(costs) - 1 - candidates
        heapq.heapify(front_pq)
        heapq.heapify(rear_pq)
        
        for i in range(k):
            if not rear_pq or front_pq and front_pq[0] <= rear_pq[0]:
                ans += heapq.heappop(front_pq)
                
                if head_ref <= tail_ref:
                    heapq.heappush(front_pq, costs[head_ref])
                    head_ref += 1
                    
            else:
                ans += heapq.heappop(rear_pq)
                
                if head_ref <= tail_ref:
                    heapq.heappush(rear_pq, costs[tail_ref])
                    tail_ref -= 1 
                    
        return ans
            
        