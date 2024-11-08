class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res=0
        visited = [[0] * len(isConnected[0]) for _ in range(len(isConnected))]

        def dfs(i,j):
            for x in range(len(visited[0])):
                if isConnected[j][x]==1 and not visited[j][x]:
                    visited[j][x]=1
                    visited[x][j]=1
                    dfs(j,x)
        res=0
        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if isConnected[i][j]==1 and not visited[i][j]:
                    visited[i][j]=1
                    visited[j][i]=1
                    res+=1
                    dfs(i,j)
        return res