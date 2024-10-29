class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dirr=[[-1,1],[0,1],[1,1]]
        res=0
        @cache
        def dfs(r,c):
            ans=1
            for x,y in dirr:
                new_x,new_y=r+x,c+y
                if new_x in range(len(grid)) and new_y in range(len(grid[0])) and grid[new_x][new_y]>grid[r][c]:
                    ans=max(ans,1+dfs(new_x,new_y))
            return ans
        for i in range(len(grid)):
            res=max(res,dfs(i,0))
        return res-1
