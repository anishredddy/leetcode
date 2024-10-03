class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        curr=i=0
        while i<len(nums):
            if nums[i]!=0:
                if curr!=i:
                    nums[curr]=nums[i]
                curr+=1
            i+=1
        

        for i in range(curr,len(nums)):
            nums[i]=0
