class Solution:
    def canSortArray(self, nums):
        prev=float('-inf')

        no=bin(nums[0]).count("1")
        max_curr=nums[0]
        min_curr=nums[0]

        for i in range(1,len(nums)):
            if bin(nums[i]).count("1")==no:
                #same
                min_curr=min(min_curr,nums[i])
                max_curr=max(max_curr,nums[i])
            else:
                #diff
                if min_curr<prev:
                    return False
                prev=max_curr

                max_curr=nums[i]
                min_curr=nums[i]
                no=bin(nums[i]).count("1")
        if min_curr<prev:
            return False
        return True
