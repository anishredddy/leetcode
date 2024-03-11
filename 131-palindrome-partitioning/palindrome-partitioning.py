class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part=[]

        mem={}
        #memorised values
        def isPalin(l,r):
            if (l,r) in mem:
                return mem[l,r]
            while l<r:
                if s[l]!=s[r]:
                    mem[l,r]=False
                    return False
                l+=1
                r-=1
            mem[l,r]=True
            return True

        def dfs(i):
            if i>=len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if isPalin(i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
            