class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        # Constants, need to be updated if the board is not 9 x 9 to get dynamic value
        rowLen = 9
        colLen = 9
        for rowIdx in range(rowLen):
            for colIdx in range(colLen):
                numstr = board[rowIdx][colIdx]
                if numstr == ".":
                    continue

                squareIdx = (rowIdx // 3) * 3 + (colIdx // 3)                
                if numstr in rows[rowIdx] or numstr in columns[colIdx] or numstr in squares[squareIdx]:
                        return False
                else:
                    rows[rowIdx].add(numstr)
                    columns[colIdx].add(numstr)
                    squares[squareIdx].add(numstr)
        
        return True


                    
