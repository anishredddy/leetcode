class Solution:
    def checkRecord(self, n):
        MOD=10**9+7

        if n==1:
            return 3
        
        res={
            (0,0):1,(0,1):1,(0,2):0,
            (1,0):1,(1,1):0,(1,2):0
        }

        for i in range(n-1):
            tmp=defaultdict(int)

            #choose P
            tmp[(0,0)]=res[(0,0)]%MOD + res[(0,1)]%MOD + res[(0,2)]%MOD
            tmp[(1,0)]=res[(1,0)]%MOD+res[(1,1)]%MOD+res[(1,2)]%MOD

            #choose L
            tmp[(0,1)]=res[(0,0)]%MOD
            tmp[(1,1)]=res[(1,0)]%MOD
            tmp[(0,2)]=res[(0,1)]%MOD
            tmp[(1,2)]=res[(1,1)]%MOD

            #choose A
            tmp[(1,0)]=tmp[(1,0)]+res[(0,0)]+res[(0,1)]+res[(0,2)]%MOD
            
            res=tmp
        return sum(res.values())%MOD