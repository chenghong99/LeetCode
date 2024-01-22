class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashmap = {}
        ans = 0
        
        for ls in grid:
            to_tup = tuple(ls)
            hashmap[to_tup] = hashmap.get(to_tup, 0) + 1
            
        for row in range(len(grid)):
            tup = ()
            for col in range(len(grid)):
                tup += (grid[col][row],)
                
            ans += hashmap.get(tup, 0)
            
        return ans
                