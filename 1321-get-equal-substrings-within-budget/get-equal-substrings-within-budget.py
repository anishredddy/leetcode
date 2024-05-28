class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        count=[]

        for i in range(len(s)):
            count.append(abs(ord(s[i])-ord(t[i])))
        
        left=right=0
        curr=res=0
        while right<len(s):
            if(count[right]+curr)<=maxCost:
                curr+=count[right]
                right+=1
            else:
                curr-=count[left]
                left+=1
            res=max(res,right-left)
        return res
    # 1 1 1 2