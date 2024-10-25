class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res=0
        n=len(nums)

        bitwise=0
        for num in nums:
            bitwise=bitwise|num

        def dfs(ind,ans):
            nonlocal res
            if ind==n:
                return
            #include
            new_ans=ans|nums[ind]
            if new_ans==bitwise:
                res+=1
            

            dfs(ind+1,new_ans)
            #dont include
            dfs(ind+1,ans)
        dfs(0,0)
        return res
