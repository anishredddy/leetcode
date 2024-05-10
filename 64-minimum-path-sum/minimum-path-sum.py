class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mem={}

        def dfs(i,j):
            if (i,j) in mem:
                return mem[(i,j)]
            
            if i==len(grid)-1 and j==len(grid[0])-1:
                return grid[i][j]
            
            left=right=float('inf')

            if i+1<len(grid):
                left=grid[i][j]+dfs(i+1,j)
            if j+1<len(grid[0]):
                right=grid[i][j]+dfs(i,j+1)
            
            mem[(i,j)]=min(left,right)
            
            return mem[(i,j)]
        return dfs(0,0)
