class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #i think this should be O(n*m) time and O(n*m) space
        #cant really think of a way without having a vistied set

        newZeroes = set()
        rows, cols = len(matrix), len(matrix[0])

        def updateZeroes(row, col):
            #set zeros on the row
            for i in range(cols):
                if matrix[row][i] != 0:
                    matrix[row][i] = 0
                    newZeroes.add((row, i))
            
            #set zeros on the column
            for i in range(rows):
                if matrix[i][col] != 0:
                    matrix[i][col] = 0
                    newZeroes.add((i, col))

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0 and (row, col) not in newZeroes:
                    updateZeroes(row, col)
        


                

        

        