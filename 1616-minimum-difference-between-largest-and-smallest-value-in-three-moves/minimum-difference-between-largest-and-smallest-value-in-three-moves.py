class Solution:
    def minDifference(self, nums: List[int]) -> int:
        #dynamic - wont work?
        #intutition - somehow use greedy


        if len(nums)<=4:
            return 0

        nums.sort()

        diff=float("inf")

        for left in range(4):
            right=len(nums)-4+left
            diff=min(nums[right]-nums[left],diff)
        return diff