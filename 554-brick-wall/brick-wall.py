class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap=defaultdict(int)
        maxEdges=0
        for i in range(len(wall)):
            prev=0
            for j in range(len(wall[i])-1):
                prev=prev+wall[i][j]
                gap[prev]+=1
                maxEdges=max(gap[prev],maxEdges)
        return len(wall)-maxEdges