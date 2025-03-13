
from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        num_rows, num_cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        INF = 2147483647
        TREASURE = 0
        OBSTACLE = -1

        # get start from the treasure 
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == TREASURE:
                    q.append((i,j))
                    visited.add((i,j))

        def addElement(i,j):
            if i < 0 or j < 0 or i == num_rows or j == num_cols or (i,j) in visited or grid[i][j] == -1 :
                return
            visited.add((i,j))
            q.append((i,j))

        distance = TREASURE
        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                grid[x][y] = distance
                addElement(x + 1,y)
                addElement(x - 1,y)
                addElement(x,y + 1)
                addElement(x,y - 1)
            distance += 1 

        return grid



input =  [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]                   
print(Solution().islandsAndTreasure(input))