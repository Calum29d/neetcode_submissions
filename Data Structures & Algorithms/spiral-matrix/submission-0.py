class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            #get every number in the current top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1 #cut off the top row

            #get every number in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1 ])
            right -= 1 #cut off the right row

            if not (left < right and top < bottom):
                break
            
            #get every number in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1 #cut off the bottom row

            #every every number in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1 #cut off the left col

        return res

     