class Solution:
    def minimumDeletions(self, s: str) -> int:
        right=[0]*len(s)
        curr=0
        for i in range(len(s)-2,-1,-1):
            if s[i+1]=='a':
                curr+=1
            right[i]=curr
        
        #found right
        left=0
        res=float('inf')

        print(right)

        for i in range(len(s)):
            # print(i,left,left+right[i])
            res=min(res,left+right[i])
            if s[i]=='b':
                left+=1
        return res
        