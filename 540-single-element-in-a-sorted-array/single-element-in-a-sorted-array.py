class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # everything even //2
        # but length will be odd cuz one number is only once
        # can take advantage of this + sorted
        # divide array and find middle most element 
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[len(nums)-1]!=nums[len(nums)-2]:
            return nums[len(nums)-1]
        low=1
        high = len(nums)-2

        while low < high:
            mid = (low +high)//2
            #found mid element
            if (mid%2==0 and nums[mid+1]==nums[mid]) or (mid%2==1 and nums[mid]==nums[mid-1]):
                # remove left half
                low=mid+1
            elif nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                # return
                return nums[mid]
            else:
                high=mid-1
                #return
        return 10