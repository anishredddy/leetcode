class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row=len(grid)
        col=len(grid[0])

        dirr=[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c):
            grid[r][c]='0'
            for new_r,new_c in dirr:
                if new_r+r in range(row) and new_c+c in range(col) and grid[new_r+r][new_c+c]=='1':
                    dfs(r+new_r,c+new_c)
        res=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1':
                    res+=1
                    dfs(r,c)
        return res