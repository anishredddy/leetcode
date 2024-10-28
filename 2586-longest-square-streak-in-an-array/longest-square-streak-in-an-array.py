class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        dp={}
        res=0
        s=set(nums)
        for num in nums:
            if num in dp:
                continue
            curr=num
            l=0
            while curr in s:
                l+=1
                dp[curr]=l
                curr*=curr
            res=max(res,l)
        return -1 if res==1 else res