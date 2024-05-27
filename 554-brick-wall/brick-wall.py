class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap=defaultdict(int)
        for i in range(len(wall)):
            prev=0
            for j in range(len(wall[i])-1):
                prev=prev+wall[i][j]
                gap[prev]+=1
        n=len(wall)
        res=float('inf')
        for val in gap.values():
            res=min(res,n-val)
        return n if res==float('inf') else res