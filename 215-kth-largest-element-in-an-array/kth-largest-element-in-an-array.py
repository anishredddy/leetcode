class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-num for num in nums]
        heapq.heapify(nums)
        i=1
        while i<k:
            heapq.heappop(nums)
            i+=1
        return -heapq.heappop(nums)