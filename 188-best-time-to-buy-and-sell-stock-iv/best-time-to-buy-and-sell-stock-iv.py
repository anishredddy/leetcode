class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        mem={}
        def dp(i,holding,remain):
            if (i,holding,remain) in mem:
                return mem[(i,holding,remain)]
            if i==len(prices) or remain==0:
                return 0
            
            #skip
            ans=dp(i+1,holding,remain)

            if holding:
                #sell
                ans=max(ans,prices[i]+dp(i+1,False,remain-1))
            else:
                #buy
                ans=max(ans,-prices[i]+dp(i+1,True,remain))
            mem[(i,holding,remain)]=ans
            return ans

        return dp(0,False,k)