class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows, cols = len(board), len(board[0])
        unSafe = set()

        def dfs(r, c):
            # base case
            if (r < 0 or r == rows 
            or c < 0 or c == cols or board[r][c] == "X" or (r, c) in unSafe):
                return
            
            unSafe.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        #start dfs on the edge O's 
        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)
            
            if board[row][cols - 1] == "O":
                dfs(row, cols - 1)
        
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col)
            
            if board[rows - 1][col] == "O":
                dfs(rows - 1, col)

        # final scan to mark the safes 'O' as X's

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in unSafe and board[r][c] == "O":
                    board[r][c] = "X"
            

        