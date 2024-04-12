class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        if n==2:
            return "11"
        
        ans="1"
        for i in range(n-1):
            next_str=''
            j=0
            while j<len(ans):
                count=1
                while j+1<len(ans) and ans[j]==ans[j+1]:
                    count+=1
                    j+=1
                next_str+=str(count)+ans[j]
                j+=1
            ans=next_str
        return next_str