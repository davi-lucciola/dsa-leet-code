from typing import List

# Time Complexity: O(n * m)
# Space Complexity: O(n + m)



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        positions_set = set()

        for i in range(m):
            for j in range(n):
                value = matrix[i][j]

                if value == 0:
                    positions_set.add((i, j))

        for i, j in positions_set:
            for row in range(m):
                matrix[row][j] = 0

            for col in range(n):
                matrix[i][col] = 0
