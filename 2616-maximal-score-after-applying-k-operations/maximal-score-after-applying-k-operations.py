class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]=-1*nums[i]
        heapq.heapify(nums)
        res=0
        for _ in range(k):
            curr=heapq.heappop(nums)
            heapq.heappush(nums,curr//3)
            res+=-1*curr
        return res