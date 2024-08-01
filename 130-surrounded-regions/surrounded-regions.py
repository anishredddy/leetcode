class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or board[r][c]!='O':
                return
            print(r,c)
            board[r][c]='A'
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        rowSet=set([0,rows-1])
        colSet=set([0,cols-1])
        
        for i in range(rows):
            for j in range(cols):
                if i in rowSet or j in colSet and board[i][j]=='O':
                    dfs(i,j)

        for row in board:
            print(row)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='A':
                    board[r][c]='O'
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c]=='A':
        #             board[r][c]='O'