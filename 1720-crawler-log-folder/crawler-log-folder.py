class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res=0
        for log in logs:
            if log=="../":
                if res>0:
                    res-=1
            elif log=="./":
                continue
            else:
                res+=1
        return res