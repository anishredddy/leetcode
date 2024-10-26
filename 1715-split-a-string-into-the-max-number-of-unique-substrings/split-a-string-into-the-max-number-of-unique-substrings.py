class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res=0
        def dfs(sett,start,i):
            nonlocal res
            if i==len(s):
                if s[start:] not in sett:
                    print(sett)
                    res=max(res,len(sett)+1)
                return
            #skip
            dfs(sett,start,i+1)

            #not skip
            if s[start:i] not in sett:
                new_set=sett.copy()
                new_set.add(s[start:i])
                dfs(new_set,i,i+1)
        a=set()
        dfs(a,0,1)
        return res