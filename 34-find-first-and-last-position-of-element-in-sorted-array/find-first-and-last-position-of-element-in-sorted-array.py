class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0

        high=len(nums)-1

        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                #inset logic
                low=high=mid
                while low>=0 and nums[low]==nums[mid]:
                    low-=1
                while high<len(nums) and nums[high]==nums[mid]:
                    high+=1
                return [max(0,low+1),min(len(nums)-1,high-1)]
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]
                