class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        pairs={}

        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                j=stack.pop()
                pairs[i]=j
                pairs[j]=i

        i,dir=0,1
        res=[]
        while i<len(s):
            if s[i]=="(" or s[i]==")":
                i=pairs[i]
                dir=-dir
            else:
                res.append(s[i])
            i+=dir
        return "".join(res)
        # ed et co el
        # ed octe el
        # leetcode