class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        a=e=i=o=u=0
        left=0
        res=0
        for right in range(len(s)):
            if s[right]=='a':
                a+=1
            if s[right]=='e':
                e+=1
            if s[right]=='i':
                i+=1
            if s[right]=='o':
                o+=1
            if s[right]=='u':
                u+=1
            na=a
            ne=e
            no=o
            ni=i
            nu=u
            left=0
            while (na%2!=0 or ne%2!=0 or ni%2!=0 or no%2!=0 or nu%2!=0) and left<=right:
                if s[left]=='a':
                    na-=1
                if s[left]=='e':
                    ne-=1
                if s[left]=='i':
                    ni-=1
                if s[left]=='o':
                    no-=1
                if s[left]=='u':
                    nu-=1
                left+=1
            res=max(res,right-left+1)
        return res