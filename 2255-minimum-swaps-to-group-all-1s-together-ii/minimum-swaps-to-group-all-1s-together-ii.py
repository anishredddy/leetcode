class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count1=0
        for num in nums:
            if num==1:
                count1+=1

        return min(self.count(nums,1,count1),self.count(nums,0,len(nums)-count1))
        
    def count(self,nums,x,count):
        res=0
        curr=0
        r=0
        for r in range(count):
            if nums[r]==x:
                res+=1
        curr=res
        l=0

        for r in range(count,len(nums)):
            if nums[r]==x:
                curr+=1
            if nums[l]==x:
                curr-=1
            l+=1
            res=max(res,curr)
        
        return count-res