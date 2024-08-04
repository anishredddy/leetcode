class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD=10**9+7
        sub=[(n,i) for i,n in enumerate(nums)]

        heapq.heapify(sub)
        
        i=1
        res=0

        while sub and i<=right:
            curr,ind=heapq.heappop(sub)
            if ind+1<n:
                heapq.heappush(sub,((curr+nums[ind+1])%MOD,ind+1))
            if i>=left:
                # print(curr)
                res=(res+curr)%MOD
            i+=1
        return res