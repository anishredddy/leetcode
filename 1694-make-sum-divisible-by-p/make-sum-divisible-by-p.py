class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n=len(nums)
        tot=sum(nums)%p
        if tot==0:
            return 0
        pre={0:-1}
        res=n
        curr=0
        for i in range(len(nums)):
            curr=(curr+nums[i])%p
            if(curr-tot+p)%p in pre:
                res=min(res,i-pre[(curr-tot+p)%p])
            pre[curr]=i
        return -1 if res==n else res