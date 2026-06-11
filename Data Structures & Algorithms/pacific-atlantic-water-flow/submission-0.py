class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, visit, prevHeight):
            #out of range, visited before or the square isnt appropriate height
            if ((row, col) in visit or row < 0 or col < 0
                or row == rows or col == cols or heights[row][col] < prevHeight):
                return
            
            #else we add the square to the appropriate set
            visit.add((row, col))
            
            #traverse all neighbors
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])

        #start dfs on the top and bottom of the grid
        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows - 1, col, atl, heights[rows - 1][col])
        
        #start dfs on the sides of the grid
        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][cols - 1])

        res = []
        #see if each square can reach both oceans
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pac and (row, col) in atl:
                    res.append([row, col])

        return res