class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #we can be greedy with our approach
        #intuition 
        # if the difference between the largest and smallest element is less than limit
        # it is guarenteed that the entire subarray difference will be less than limit

        #how to do?
        
        #approch 1:

        #maintain 2 heaps, max heap and min heap?

        # how to implement this?
        
        #keep adding elements in max heap and min heap, check untill condition max-min<=limit

        #how to deal with when we break the condition? remove max or min?

        #since we are checking continuos , pop the first element , max or min..?

        min_heap=[]
        max_heap=[]

        left=0
        res=0

        for right in range(len(nums)):
            heapq.heappush(min_heap,(nums[right],right))
            heapq.heappush(max_heap,(-nums[right],right))

            while -max_heap[0][0]-min_heap[0][0]>limit:
                left=min(min_heap[0][1],max_heap[0][1])+1

                while max_heap[0][1]<left:
                    heapq.heappop(max_heap)

                
                while min_heap[0][1]<left:
                    heapq.heappop(min_heap)
            res=max(res,right-left+1)
        return res