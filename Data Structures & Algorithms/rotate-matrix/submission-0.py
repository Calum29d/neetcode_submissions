class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        #set the boundaries
        l, r = 0, len(matrix[0]) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                #save the top left as temp
                topLeft = matrix[top][l + i]

                #move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                #move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                #move top right into bottom left
                matrix[bottom][r - i] = matrix[top + i][r]

                #move top left into top right
                matrix[top + i][r] = topLeft
            
            r -= 1
            l += 1

        #O(n^2) time and O(1) space