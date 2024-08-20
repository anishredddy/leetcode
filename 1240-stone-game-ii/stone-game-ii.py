class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        mem={}
        def dfs(alice,i,M):
            if i==len(piles):
                return 0

            if (alice,i,M) in mem:
                return mem[(alice,i,M)]
            
            res=0 if alice else float('inf')

            tot=0

            for x in range(1,2*M+1):
                if i+x>len(piles):
                    break
                tot+=piles[i+x-1]
                if alice:
                    res=max(res,tot+dfs(not alice,i+x,max(M,x)))
                else:
                    res=min(res,dfs(not alice,i+x,max(M,x)))
            mem[(alice,i,M)]=res
            return res
        return dfs(True,0,1)