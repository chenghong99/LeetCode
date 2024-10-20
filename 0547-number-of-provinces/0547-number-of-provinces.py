from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0 
        
        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                q = deque()
                q.append(i)
                while len(q) != 0:
                    first = q.popleft()
                    for j in range(len(isConnected[first])):
                        if isConnected[first][j] == 1 and j not in visited:
                            visited.add(j)
                            q.append(j)
        return count
        
        