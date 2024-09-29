class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k==0:
            return 0
        if k>=len(prices)//2:
            res=0
            for i in range(1,len(prices)):
                if(prices[i-1]<prices[i]):
                    res+=prices[i]-prices[i-1]
            return res
        dp = [[0] * len(prices) for _ in range(k + 1)]

        for i in range(1,k+1):
            diff=-prices[0]
            for j in range(1,len(prices)):
                dp[i][j]=max(dp[i][j-1],prices[j]+diff)
                diff=max(diff,dp[i-1][j]-prices[j])
        return dp[k][len(prices)-1]