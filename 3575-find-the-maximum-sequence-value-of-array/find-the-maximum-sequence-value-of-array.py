class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        # nums[i] <^7 => max 7 bits
        n=len(nums)

        def generate_combinations(nums):
            t1={(0,0)}
            d={}
            for ind,num in enumerate(nums):
                t2=set()
                for taken,value in t1:
                    if taken<k:
                        t2.add((taken+1,value|num))
                        if taken+1==k and value|num not in d:
                            d[value|num]=ind+1
                t1.update(t2)
            return d
        
        a=generate_combinations(nums)
        b=generate_combinations(nums[::-1])

        res=float('-inf')
        for v1,x1 in a.items():
            for v2,x2 in b.items():
                if x1+x2<=n:
                    res=max(res,v1^v2)
        return res