class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)==0:
            return 0

        nums.sort()

        res=1
        temp=1
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]+1:
                temp+=1
            elif i>0 and nums[i]==nums[i-1]:
                continue
            else:
                temp=1
            res=max(res,temp)
        return res