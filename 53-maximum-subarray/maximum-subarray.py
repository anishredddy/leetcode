class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]

        total=0
        for num in nums:
            total+=num
            res=max(total,res)
            if total<0:
                total=0
        return res