class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        LEN = 9
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        
        for r in range(LEN):
            for c in range(LEN):
                cur_cell = board[r][c] 
                if cur_cell == ".": continue

                # Check if current cell has a duplicate in 
                # rows, cols, or in its current 3 by 3 square.
                if ( cur_cell in rows[r]
                    or cur_cell in cols[c]
                    or cur_cell in squares[(r // 3, c // 3)] ):
                    return False
                
                # Since current cell is not yet in its sudoku row, col, 
                # current 3 by 3 square, add it to all of the hashsets.
                cols[c].add(cur_cell)
                rows[r].add(cur_cell)
                squares[(r // 3, c // 3)].add(cur_cell)

        return True
