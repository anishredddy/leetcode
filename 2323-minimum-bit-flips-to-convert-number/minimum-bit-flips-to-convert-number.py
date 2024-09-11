class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s=bin(start)[2:]
        g=bin(goal)[2:]
        if len(s)>len(g):
            g='0'*(len(s)-len(g))+g
        else:
            s='0'*(len(g)-len(s))+s
        res=0
        for i in range(len(s)):
            if s[i]!=g[i]:
                res+=1
        return res        