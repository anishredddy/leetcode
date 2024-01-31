class Solution:
    def merge(self, intervals):
        intervals=sorted(intervals,key=lambda x:x[0])
        print(intervals)
        l,r=intervals[0][0],intervals[0][1]
        res=[]
        for i in range(1,len(intervals)):
            if r<intervals[i][0]:
                res.append([l,r])
                l=intervals[i][0]
                r=intervals[i][1]
            else:
                r=max(r,intervals[i][1])
        res.append([l,r])
        return res