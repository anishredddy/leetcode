class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree=[0]*n
        for u,v in edges:
            indegree[v]+=1
        res=-1
        for i in range(len(indegree)):
            if indegree[i]==0:
                if res!=-1:
                    return -1
                res=i
        return res