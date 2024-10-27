from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ## for each pos look up down left and right for possible paths and add to queue        
        queue = deque()
        visited = set()
        entrance.append(0)
        queue.append(entrance)
        
        while len(queue) > 0:
            first = queue.popleft()
            if (first[0] == 0 or first[0] == len(maze) - 1 or first[1] == 0 or first[1] == len(maze[0]) - 1):
                if (first[0] != entrance[0] or first[1] != entrance[1]):
                    return first[2]
            up = [first[0]-1, first[1], first[2]+1]
            if tuple(up[:2]) not in visited and first[0]-1 >= 0 and maze[up[0]][up[1]] != '+':
                visited.add(tuple(up[:2]))
                queue.append(up)
            down = [first[0]+1, first[1], first[2]+1]
            if tuple(down[:2]) not in visited and first[0]+1 <= len(maze)-1 and maze[down[0]][down[1]] != '+':
                visited.add(tuple(down[:2]))
                queue.append(down)
            left = [first[0], first[1]-1, first[2]+1]
            if tuple(left[:2]) not in visited and first[1]-1 >= 0 and maze[left[0]][left[1]] != '+':
                visited.add(tuple(left[:2]))
                queue.append(left)
            right = [first[0], first[1]+1, first[2]+1]
            if tuple(right[:2]) not in visited and first[1]+1 <= len(maze[0])-1 and maze[right[0]][right[1]] != '+':
                visited.add(tuple(right[:2]))
                queue.append(right)
           
            
        return -1