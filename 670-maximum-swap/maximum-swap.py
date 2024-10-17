class Solution:
    def maximumSwap(self, num: int) -> int:
        s=str(num)
        res=[0]*len(s)
        for i in range(len(s)-1,-1,-1):
            if i<len(s)-1:
                if res[i+1][0]>=int(s[i]):
                    res[i]=res[i+1]
                else:
                    res[i]=[int(s[i]),i]
            else:
                res[i]=[int(s[i]),i]
        for i in range(len(s)):
            if res[i][0]>int(s[i]):
                return int(s[:i]+s[res[i][1]]+s[i+1:res[i][1]]+s[i]+s[res[i][1]+1:])
        return int(s)