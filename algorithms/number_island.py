"""
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).
"""
from typing import List
 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        number_of_islands = int()
        num_rows, num_columns = len(grid), len(grid[0])
        def dfs(i, j):
            if  i < 0 or i == num_rows or j < 0 or j == num_columns or (i,j) in visited or grid[i][j] == "0":
                return 0

            visited.add((i,j))

            return dfs(i, j +1) or dfs(i + 1,j) or dfs(i,j-1 )  or dfs(i-1 ,j ) 
        


        for rows in range(num_rows):
            for columns in range(num_columns):
                if grid[rows][columns] == "1" and (rows,columns) not in visited:
                    number_of_islands += 1 
                    dfs(rows,columns)

        return number_of_islands
# grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
grid=[["1","1","0","0","1"],["1","1","0","0","1"],["0","0","1","0","0"],["0","0","0","1","1"]]

print(Solution().numIslands(grid))