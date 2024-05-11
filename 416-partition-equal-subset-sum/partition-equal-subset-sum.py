class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2:
            return False
        target=s//2

        for num in nums:
            if num==target:
                return True
            if num>target:
                return False

        # lets try memorisation

        dp=[[0 for _ in range(target+1)] for _ in range(len(nums))]


        n=len(nums)
        for i in range(n):
            dp[i][0]=True

        dp[0][nums[0]]=True
    
        for i in range(1,n):
            for j in range(1,target+1):
                curr=dp[i-1][j]
                picked=False
                if j>=nums[i]:
                    picked=dp[i-1][j-nums[i]]
                dp[i][j]=curr or picked
        return dp[n-1][target]