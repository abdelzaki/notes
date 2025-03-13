
"""
You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.
"""
from typing import List
import math


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        self.area = 0
        num_rows , num_columns = len(grid), len(grid[0])

        def dfs(i, j):
            if  i < 0 or i == num_rows or j < 0 or j == num_columns or (i,j) in visited or grid[i][j] == 0:
                return 0 
            visited.add((i,j))
            self.area += 1
            return dfs(i, j +1) or dfs(i + 1,j) or dfs(i,j-1 )  or dfs(i-1 ,j ) 


        for i in range(num_rows):
            for j in range(num_columns):
                if grid[i][j] == 1 and (i,j) not in visited:
                    self.area = 0
                    dfs(i,j)     
                    max_area = max(self.area, max_area)
        return max_area

grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

solution = Solution()
print(solution.maxAreaOfIsland(grid))