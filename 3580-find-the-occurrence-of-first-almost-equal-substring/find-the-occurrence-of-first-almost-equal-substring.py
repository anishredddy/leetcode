def z_algo(s: str) -> List[int]: 
    """Z-algorithm
    Return lengths of substrings that are also prefix strings."""
    z=[0]*len(s)
    l=r=k=0
    for i in range(len(s)):
        if i>r:
            # outside z box
            l=r=i
            while r<len(s) and s[r]==s[r-i]:
                r+=1
            z[i]=r-l
            r-=1
        else:
            k=i-l
            if z[k]<r-i+1:
                z[i]=z[k]
            else:
                l=i
                while r<len(s) and s[r]==s[r-l]:
                    r+=1
                #increase size of z-box
                z[i]=r-l
                r-=1
    return z


class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        n = len(s)
        k = len(pattern)
        prefix = z_algo(pattern + "#" + s)[k+1:]
        suffix = z_algo(pattern[::-1] + "#" + s[::-1])[k+1:][::-1]
        for i in range(n-k+1): 
            if prefix[i] + suffix[i+k-1] >= k-1: return i
        return -1