class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
        def dfs(i,visited):
            if i in visited:
                return
            visited.add(i)
            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei,visited)
        for i in range(n):
            visited=set()
            dfs(i,visited)
            if len(visited)==n:
                return i
        return -1