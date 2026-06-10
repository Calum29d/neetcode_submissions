class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        numOfIslands = 0

        def dfs(row, col):
            #if we are out of boundary or the adjacent square is not part of the island
            if (row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0"):
                return

            #vist the part of the island and mark it as visited
            grid[row][col] = "0"

            #explore all adjacent squares
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col -1)
        
        #start the dfs once we find the start of an island
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    numOfIslands += 1
                    dfs(row, col)

        return numOfIslands
                    




        