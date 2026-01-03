class Solution:
    def numOfWays(self, n: int) -> int:
        MOD=10**9+7
        def valid_row(grid):
            if grid[0]!=grid[1] and grid[1]!=grid[2]:
                return True
            return False
        
        valid_comb=[]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if valid_row([i,j,k]):
                        valid_comb.append((i,j,k))
        @lru_cache
        def dfs(i,prev):
            if i==n:
                return 1
            ans=0
            for r in valid_comb:
                if r[0]!=prev[0] and r[1]!=prev[1] and r[2]!=prev[2]:
                    ans=(ans+dfs(i+1,r))%MOD
            return ans
        return dfs(0,(-1,-1,-1))