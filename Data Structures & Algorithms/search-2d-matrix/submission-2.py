class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break #found the row the target is in so break out
            
            
        if not (top <= bot): #no row contains target
            return False 
        
        row = (top + bot) // 2
        start, end = 0, cols - 1

        #then binary search on the row found
        while start <= end:
            mid = (start + end) // 2

            if target > matrix[row][mid]:
                start = mid + 1
            elif target < matrix[row][mid]:
                end = mid - 1
            else:
                return True
        
        return False

        #O(log(n*m)) time O(1) space


