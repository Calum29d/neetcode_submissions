class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        res = 0
        
        self.rows, self.cols = len(grid), len(grid[0])

        def dfs(r, c):
            # base case, out of bounds or not on land
            if r >= self.rows or c >= self.cols or r < 0 or c < 0 or grid[r][c] == 0:
                return 0

            # visit current land
            grid[r][c] = 0
            
            # start dfs on all directions
            islandCount = 1 + (dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

            return islandCount
        

        # start dfs on all islands
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))
        
        return res

        # Time: O(rows * cols) 
        # Space: O(rows * cols)
            

        