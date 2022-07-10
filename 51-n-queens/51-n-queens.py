class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiagonal = set()
        negDiagonal = set()
        result = []
        board = [["."] * n for i in range(n)]
        
        def dfs(r):
            if r == n:
                boardCopy = ["".join(row) for row in board]
                result.append(boardCopy)
                return
            for i in range(n):
                if (i in cols) or ((r+i) in posDiagonal) or ((r-i) in negDiagonal):
                    continue
                    
                cols.add(i)
                posDiagonal.add(r+i)
                negDiagonal.add(r-i)
                board[r][i] = 'Q'

                dfs(r+1)
                
                cols.remove(i)
                posDiagonal.remove(r+i)
                negDiagonal.remove(r-i)
                board[r][i] = "."
        
        dfs(0)
        return result