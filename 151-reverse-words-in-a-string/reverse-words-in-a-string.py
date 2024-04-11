class Solution:
    def reverseWords(self, s: str) -> str:
        stack=[]
        i=0
        while s[i]==" ":
            i+=1
        j=len(s)-1
        while s[j]==" ":
            j-=1
        y=""
        for x in range(i,j+1):
            if s[x]==" " and s[x-1]!=" ":
                stack.append(y)
                y=""
            elif x==j:
                y+=s[x]
                stack.append(y)
            elif s[x]!=" ":
                y+=s[x]
        res=""
        while stack:
            res+=stack.pop()
            res+=" "
        return res[:len(res)-1]