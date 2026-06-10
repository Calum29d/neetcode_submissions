class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        currentPath = set()
        rows, cols = len(board), len(board[0])

        def dfs(row, col, i):
            #if we have found every letter in the word
            if i == len(word):
                return True
            
            #if we are out of bounds or the letter is not in the word or we have visited that path before then dont carry on
            if(row < 0 or col < 0 or row >= rows or col >= cols or word[i] != board[row][col] or (row, col) in currentPath):
                return False

            #vist the current square
            currentPath.add((row, col))

            #go through every direction from the current square
            res = (dfs(row + 1, col, i + 1) or
                    dfs(row - 1, col, i + 1) or
                    dfs(row, col + 1, i + 1) or
                    dfs(row, col - 1, i + 1))
            #backtrack by removing the currentPath as we will need to visit it in different loops
            currentPath.remove((row, col))
            return res
        
        #start the dfs from every square 
        for row in range(rows):
            for col in range(cols):
                #only execute if we have found the start of word
                if board[row][col] == word[0]:
                    if dfs(row, col, 0): return True

        return False

            

            



        