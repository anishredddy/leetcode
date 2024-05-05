class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        colours=[0]*n


        def dfs(node,colour):
            if colours[node] !=0:
                return colours[node]==colour
            
            colours[node]=colour

            for nei in graph[node]:
                if not dfs(nei,-colour):
                    return False
            
            return True
        for i in range(n):
            if colours[i]==0:
                if not dfs(i,1):
                    return False
        return True