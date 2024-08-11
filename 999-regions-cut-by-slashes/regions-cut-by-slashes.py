class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        matrix=[[0]*(cols*3) for _ in range(rows*3)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x=i*3
                y=j*3
                if grid[i][j]=='/':
                    matrix[x+2][y]=1
                    matrix[x+1][y+1]=1
                    matrix[x][y+2]=1
                elif grid[i][j]=='\\':
                    matrix[x][y]=1
                    matrix[x+1][y+1]=1
                    matrix[x+2][y+2]=1
        res=0

        for row in matrix:
            print(row)

        dirr=[[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(i,j):
            matrix[i][j]=1
            for x,y in dirr:
                if x+i in range(len(matrix)) and y+j in range(len(matrix[0])) and matrix[x+i][y+j]==0:
                    dfs(x+i,y+j)
            return
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    res+=1
                    dfs(i,j)
        return res