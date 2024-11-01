class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x:x[0])

        r=len(robot)
        f=len(factory)

        @cache
        def dfs(rob,fac):
            if rob==r:
                return 0
            if fac==len(factory):
                return float('inf')
            cost=0
            res=float('inf')

            for i in range(factory[fac][1]+1):
                if rob+i>=r:
                    res=min(res,cost)
                    break
                res=min(res,dfs(rob+i ,fac+1)+cost)
                cost+=abs(factory[fac][0]-robot[rob+i])
                
            return res

        return dfs(0,0)