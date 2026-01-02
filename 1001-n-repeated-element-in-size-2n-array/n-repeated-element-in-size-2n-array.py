class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for num in nums:
            d[num]+=1
            if d[num]>1:
                return num