class Solution:
    def minSteps(self, n: int) -> int:
        #1D dp

        dp=[float('inf')]*(n+1)
        dp[1]=0

        for i in range(2,n+1):
            for j in range(1,1+(i//2)):
                if i%j==0:
                    dp[i]=min(dp[j]+i//j,dp[i])
        return dp[n]