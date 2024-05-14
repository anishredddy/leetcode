class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        s=0
        res=float('inf')

        for right in range(len(nums)):
            s+=nums[right]

            while s>=target:
                res=min(res,right-left+1)
                s-=nums[left]
                left+=1
        return res if res!=float('inf') else 0