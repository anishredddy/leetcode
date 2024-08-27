class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph=defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append([succProb[i],edges[i][1]])
            graph[edges[i][1]].append([succProb[i],edges[i][0]])
        
        
        def dijkstra():
            heap=[[-1,start_node]]

            dist=[0]*n
            dist[start_node]=1

            while heap:
                prob,curr=heapq.heappop(heap)
                if -1*prob < dist[curr]:
                    continue
                if curr==end_node:
                    return -1*prob
                for wei,nei in graph[curr]:
                    new_prob=prob*wei*-1
                    if new_prob>dist[nei]:
                        dist[nei]=new_prob
                        heapq.heappush(heap,[-new_prob,nei])
            return 0

        return dijkstra()
