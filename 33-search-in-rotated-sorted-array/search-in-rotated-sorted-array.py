class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        low=0
        high=len(nums)-1
        

        while low<=high:
            # runnig binary search
            mid=(low+high)//2

            if nums[mid]==target:
                return mid
            if nums[low]<=nums[mid]:
                # left half is sorted
                if target>=nums[low] and target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                #right part is sorted
                if target>=nums[mid] and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1