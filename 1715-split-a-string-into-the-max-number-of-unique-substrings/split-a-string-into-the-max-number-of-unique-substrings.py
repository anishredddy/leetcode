class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res=0
        def dfs(sett,start,i):
            nonlocal res
            if i==len(s):
                if s[start:] not in sett:

                    res=max(res,len(sett)+1)
                return
            #no skip
            if s[start:i] not in sett:
                sett.add(s[start:i])
                dfs(sett,i,i+1)
                sett.remove(s[start:i])
            #skip
            dfs(sett,start,i+1)
        a=set()
        dfs(a,0,1)
        return res