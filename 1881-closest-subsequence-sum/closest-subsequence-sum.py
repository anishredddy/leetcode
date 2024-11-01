class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        
        def dfs(nums):
            ans={0}
            for x in nums:
                ans|={x+y for y in ans}
            return ans
        
        left=dfs(nums[:len(nums)//2])
        right=sorted(dfs(nums[len(nums)//2:]))

        res=float('inf')
        for s in left:
            pos=bisect_left(right,goal-s)

            if pos<len(right):
                res=min(res,abs(goal-(s+right[pos])))
            
            if pos>0:
                res=min(res,abs(goal-(s+right[pos-1])))
        return res