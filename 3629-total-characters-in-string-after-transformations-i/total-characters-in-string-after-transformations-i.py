class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        @cache
        def dfs(s,t):
            res=0
            for char in s:
                if ord(char)+t<=ord('z'):
                    res+=1
                else:
                    new=t-(ord('z')-ord(char)+1)
                    res+=dfs("ab",new)
            return res
        return dfs(s,t)%((10**9)+7)