class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 4 2 3 5

        #we can be greedy with our approach
        #intuition 
        # if the difference between the largest and smallest element is less than limit
        # it is guarenteed that the entire subarray difference will be less than limit


        #lets try to use a deque , cuz retrieval and adding time is O(1)

        min_deque=deque()
        max_deque=deque()

        left=res=0

        for right in range(len(nums)):
            while max_deque and max_deque[-1]<nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            while min_deque and min_deque[-1]>nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            while max_deque[0]-min_deque[0]>limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left+=1
            res=max(res,right-left+1)
        return res


