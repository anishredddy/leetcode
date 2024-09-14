class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=max(nums)
        prev=float('inf')
        count=res=0
        for num in nums:
            if num==n:
                count+=1
            else:
                count=0
            res=max(count,res)
        return res