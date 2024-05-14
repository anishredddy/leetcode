class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        visited=set()

        def dfs(i,j):
            if i not in range(len(grid)) or j not in range(len(grid[0])):
                return 0
            if (i,j) in visited:
                return 0
            if grid[i][j]==0:
                return 0
            curr=grid[i][j]
            visited.add((i,j))
            path1=dfs(i+1,j)
            path2=dfs(i,j+1)
            path3=dfs(i-1,j)
            path4=dfs(i,j-1)
            visited.remove((i,j))

            return max(path1,path2,path3,path4)+curr
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0 and (i,j) not in visited:
                    res=max(res,dfs(i,j))
        return res