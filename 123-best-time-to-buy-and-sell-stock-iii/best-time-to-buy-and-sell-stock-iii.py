class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp1=[0]*len(prices)
        dp2=[0]*len(prices)
        start=0
        dp1[0]=0
        for i in range(1,len(prices)):
            dp1[i]=max(dp1[i-1],prices[i]-prices[start])
            if prices[i]<prices[start]:
                start=i

        prices=prices[::-1]
        start=0
        dp2[0]=0
        for i in range(1,len(prices)):
            dp2[i]=max(dp2[i-1],prices[start]-prices[i])
            if prices[i]>prices[start]:
                start=i
        dp2=dp2[::-1]

        # print(dp1)
        # print(dp2)

        res=0
        for i in range(len(dp1)):
            res=max(res,dp1[i]+dp2[i])
        return res