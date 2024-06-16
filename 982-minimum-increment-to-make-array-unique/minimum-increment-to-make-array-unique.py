class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        res = 0
        
        # The minimum value the next element should be
        expected = nums[0]
        
        for num in nums:
            if num < expected:
                res += expected - num
            else:
                expected = num
            expected += 1
        
        return res
