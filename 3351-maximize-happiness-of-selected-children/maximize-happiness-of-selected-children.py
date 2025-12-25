import heapq

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
    
        res=heapq.nlargest(k,happiness)
        
        ans=0
        for i in range(k):
            ans+=max(0,res[i]-i)
        return ans