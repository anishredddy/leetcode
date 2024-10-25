class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res=defaultdict(int)
        for num in nums:
            res[0]=1
            for key,val in [*res.items()]:
                res[key|num]+=val
        return res[max(res.keys())]