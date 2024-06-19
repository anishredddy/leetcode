class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        left=min(bloomDay)
        right=max(bloomDay)

        def count(x):
            temp=res=0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=x:
                    temp+=1
                else:
                    temp=0
                if temp==k:
                    temp=0
                    res+=1
            return res>=m
        while left<=right:
            mid=(left+right)//2
            c=count(mid)
            if c:
                right=mid-1
            else:
                left=mid+1
        
        return left