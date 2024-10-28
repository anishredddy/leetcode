class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(-1, n):
            d, m = 0, 1
            for j in range(n):
                if j != i:
                    d = gcd(d, nums[j])
                    m = lcm(m, nums[j])
            res = max(res, d * m)
        return res