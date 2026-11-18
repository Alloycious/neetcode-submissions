class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Treat the entire 2D matrix as a long running array
        ROWS, COLS = len(matrix), len(matrix[0])

        # Flatten the 2D matrix by multiplying ROWS by COLS to give total length
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            m = (l + r) // 2

            # Access of the flattened 2D matrix is as follows.
            # Use division identity since every row contributes exactly COLS elements before the next row starts.

            row, col = m // COLS, m % COLS

            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True

        return False
