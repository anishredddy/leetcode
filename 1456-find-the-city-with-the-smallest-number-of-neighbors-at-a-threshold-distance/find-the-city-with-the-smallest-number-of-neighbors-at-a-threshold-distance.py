class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj=defaultdict(list)
        for fro,to,weight in edges:
            adj[fro].append([to,weight])
            adj[to].append([fro,weight])


        def dijkistra(node):
            heap=[(0,node)]

            visited=set()

            while heap:
                dist,curr_node=heapq.heappop(heap)
                if curr_node in visited:
                    continue
                
                visited.add(curr_node)

                for nei,d in adj[curr_node]:
                    if d+dist<=distanceThreshold:
                        heapq.heappush(heap,(d+dist,nei))
            return len(visited)
        count=float('inf')
        res=-1
        for i in range(n):
            curr=dijkistra(i)
            if curr<count:
                count=curr
                res=i
            elif curr==count:
                res=max(res,i)
        return res