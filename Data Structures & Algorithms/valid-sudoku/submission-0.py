import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key = (row // 3, col // 3) which gives us the square

        for row in range(9):
            for col in range(9):

                #emtpy position
                if board[row][col] == ".":
                    continue
                
                #if duplicate is found in any of the rules
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or 
                    board[row][col] in squares[(row // 3, col // 3)] ):
                    return False
                
                #add the seen number to sets
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        
        return True
        

        #O(n^2) time and space



        