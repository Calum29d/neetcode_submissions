class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #transpose the matrix then reverse the rows which will rotate the matrix by 90 deg

        rows = len(matrix)
        matrix.reverse() #reverse the matrix

        for r in range(rows):
            for c in range(r, rows):
                #now transpose the matrix, making each row equal equal the column
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


        #O(n^2) time and O(1) space