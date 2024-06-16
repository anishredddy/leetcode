class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # 1 2 3 -6  if we add 5
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        # 8
        # 9
        # 10
        # 11
        # mathematically if we want to increase range [0,n] we should add a number less than or equal to n
        # then new range will be n+k
        nums.sort()
        #nlogn
        r=0
        pointer=0
        res=0
        while r<n:
            if pointer<len(nums) and nums[pointer]<=r+1:
                r+=nums[pointer]
                pointer+=1
            else:
                res+=1
                r+=r+1
        return res