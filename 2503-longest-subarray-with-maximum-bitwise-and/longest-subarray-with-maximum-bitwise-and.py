class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res=count=0
        currmax=float('-inf')
        for num in nums:
            if num>currmax:
                res=1
                count=1
                currmax=num
            elif num==currmax:
                count+=1
                res=max(count,res)
            else:
                count=0
        return res