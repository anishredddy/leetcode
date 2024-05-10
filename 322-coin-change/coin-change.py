class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins)==1:
            if amount%coins[0]!=0:
                return -1
            return amount//coins[0]
        if amount==0:
            return 0
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        coins.sort()
        m=-1
        for i in range(len(coins)):
            m=i
            if coins[i]>=amount:
                break

        for i in range(m):
            dp[coins[i]]=1

        for i in range(amount+1):

            for amt in coins:
                if amt>i:
                    break
                dp[i]=min(dp[i],dp[i-amt]+1)
        
        return int(dp[amount]) if dp[amount]!=float('inf')  else -1