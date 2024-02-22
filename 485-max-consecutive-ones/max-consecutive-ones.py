class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #1 pointer approach

        #time O(n)
        #space O(1)

        res=0
        count=0
        for r in range(len(nums)):
            if nums[r]==1:
                count+=1
                res=max(res,count)
            else:
                count=0
        return res