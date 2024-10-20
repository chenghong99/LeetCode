from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        ## initialize the queue with the first item room can visit 
        visited = set()
        q = deque()
        visited.add(0)
        q.extend(rooms[0])
        
        while len(q) != 0:
            first = q.popleft()
            if first not in visited:
                visited.add(first)
                q.extend(rooms[first])
            else:
                continue
                
            
        return len(visited) == len(rooms) 
            
        
        