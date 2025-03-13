from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        visited = set()
        reachUpOrleft  = set()
        reachDownOrRight  = set() 
        ok = set()

        num_rows, num_columns = len(heights), len(heights[0])      
        def dfs(i,j, history = []):
            new_h = history.copy()
            new_h.append((i,j))
            if i == 1 and  j ==4:
                pass
            if i == 0 or j == 0 or (i,j) in reachUpOrleft :
                for element in  new_h:
                    reachUpOrleft.add(element)
            
            if i == (num_rows -1) or j == (num_columns -1) or (i,j) in reachDownOrRight:
                for element in  new_h:
                    reachDownOrRight.add(element)
                  

            if ( (i,j) in  reachUpOrleft) and ((i,j) in  reachDownOrRight):
                for element in  new_h:
                    if ( (i,j) in  reachUpOrleft) and ((i,j) in  reachDownOrRight):
                        ok.add((i,j))
                return 
                        
            if (i,j) in visited:
                return
            visited.add((i,j))

            if  i < (num_rows -1) and heights[i][j] >= heights[i + 1][j]:
                dfs(i+1,j,new_h)
            if i >0 and heights[i][j] >= heights[i - 1][j]:
                dfs(i-1,j,new_h)
            if  j < (num_columns -1 ) and heights[i][j] >= heights[i][j +1]:
                dfs(i,j + 1,new_h)
            if j > 0 and heights[i][j] >= heights[i][j -1]:
                dfs(i,j - 1, new_h)
            
        for i in range(num_rows):
            for j in range(num_columns):
                dfs(i ,j)
            
        for element in reachDownOrRight:
            if element in reachUpOrleft:
                ok.add(element)

        return ok               
                
# heights = [
#   [4,2,7,3,4],
#   [7,4,6,4,7],
#   [6,3,5,3,6]
# ]

heights_2=[
            [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]
        ]

# [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

solution = Solution()
# print(solution.pacificAtlantic(heights))
print(solution.pacificAtlantic(heights_2))
