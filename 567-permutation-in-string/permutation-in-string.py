class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        first = [0] * 26
        for char in s1:
            first[ord(char) - ord('a')] += 1
        curr=[0]*26
        low=0
        high=len(s1)
        for i in range(high):
            curr[ord(s2[i]) - ord('a')] += 1
  
        while high<len(s2):
          if curr==first:
            return True
          curr[ord(s2[low])-ord('a')]-=1
          low+=1
          
          curr[ord(s2[high])-ord('a')]+=1
          high+=1
        if curr==first: return True
        return False
