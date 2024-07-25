class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points=sorted(points,key=lambda x:x[0])
        curr_l=points[0][0]
        curr_r=points[0][1]
        res=1
        for left,right in points[1:]:
            if left>=curr_l and left<=curr_r:
                curr_l=max(left,curr_l)
                curr_r=min(right,curr_r)
            else:
                curr_l=left
                curr_r=right
                res+=1
        return res