class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colours = [0] * n
        
        q = deque()
        
        for i in range(n):
            if colours[i] != 0:
                continue
            
            colours[i] = 1
            q.append(i)
            
            while q:
                curr = q.popleft()
                for nei in graph[curr]:
                    if colours[nei] == 0:  
                        colours[nei] = -colours[curr]
                        q.append(nei)
                    elif colours[nei] == colours[curr]:  
                        return False
                    
        return True