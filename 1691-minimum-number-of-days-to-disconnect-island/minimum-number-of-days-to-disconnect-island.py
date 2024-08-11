class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        #answer may be 0,1,2
        dirr=[[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c,visit):
            if r not in range(rows) or c not in range(cols) or grid[r][c]==0 or (r,c) in visit:
                return
            visit.add((r,c))

            for x,y in dirr:
                dfs(x+r,y+c,visit)
        
        visit=set()
        count=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r,c) not in visit:
                    dfs(r,c,visit)
                    count+=1
        if count!=1:
            return 0
        land=list(visit)

        for r,c in land:
            grid[r][c]=0
            visit=set()
            count=0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] and (i,j) not in visit:
                        dfs(i,j,visit)
                        count+=1
            if count!=1:
                return 1
            grid[r][c]=1
        return 2