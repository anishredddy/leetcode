class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count=0
        for i in range(len(s)):
            if s[i]=='a':
                a_count+=1
        # print(right)
        res=float('inf')
        left=0
        for i in range(len(s)):
            # print(i,left,left+right[i])
            if s[i]=='a':
                a_count-=1
            res=min(res,left+a_count)
            if s[i]=='b':
                left+=1
        return res
        