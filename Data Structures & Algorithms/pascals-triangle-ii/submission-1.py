class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #O(n^2) time O(n) space
        row = [1]

        for i in range(rowIndex):
            temp = [0] + row + [0]
            row = []
            for j in range(len(temp) - 1):
                row.append(temp[j] + temp[j + 1])
        return row
        