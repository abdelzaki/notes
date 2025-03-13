from typing import List
"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""


class Solution:
    def my_solution_islandPerimeter(self, grid: List[List[int]]) -> int:
        lenght_of_side = 1 
        permieter = 0
        for index, row in enumerate(grid):
            for i in range(len(row)):
                if row[i] == 1:
                    # check before cell 
                    if i == 0 or grid[index][i-1] == 0:
                        permieter += 1
                    # check right 
                    if i == len(row) -1 or grid[index][i+1] == 0:
                        permieter += 1
                    
                    # check above cell 
                    if index == 0  or grid[index-1][i] == 0:
                        permieter += 1
                    # check below cell 
                    if index == len(grid) -1  or grid[index+1][i] == 0:
                        permieter += 1
        return permieter

    def neetcode_islandPerimeter(self, grid: List[List[int]]) -> int:
        # get size
        visited = set()
        num_rows , num_columns = len(grid), len(grid[0]) 
        def dfs(i :int , j : int):
            # basic case
            if i < 0 or j < 0 or i == num_rows or j == num_columns or grid[i][j] == 0:
                return 1
            
            if (i,j) in visited:
                return 0

            visited.add((i,j))

            return dfs(i,j+1) + dfs(i+1,j)+ dfs(i, j-1) + dfs(i-1,j)  

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][i]:
                    return dfs(i,j)

grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
        ] 
grid_2 = [[0,0,0,0],
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0]
        ] 
solution = Solution()
print(solution.islandPerimeter(grid))
print(solution.islandPerimeter(grid_2))
