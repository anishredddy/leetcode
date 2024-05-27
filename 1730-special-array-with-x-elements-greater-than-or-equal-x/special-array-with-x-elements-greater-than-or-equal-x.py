class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        n=len(nums)
        ind=0
        current=nums[ind]
        for i in range(1,n+1):
            while i>current:
                ind+=1
                if ind in range(n):
                    current=nums[ind]
                else:
                    return -1
            if len(nums)-ind==i:
                return i
        return -1
