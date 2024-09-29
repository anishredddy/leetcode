class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        if s=="":
            return ""
        size=1
        start=0
        for i in range(len(s)):
            l,r=i-size,i+1
            s1,s2=s[l-1:r],s[l:r]
            if l>=1 and s1==s1[::-1]:
                size+=2
                start=l-1
            elif l>=0 and s2==s2[::-1]:
                size+=1
                start=l
        return s[start:start+size]