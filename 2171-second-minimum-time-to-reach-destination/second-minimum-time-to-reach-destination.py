class Solution:

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph=defaultdict(list)
        for i in range(len(edges)):
            node1,node2=edges[i]
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        count=0
        start=1


        q=deque()
        q.append(1)

        currTime=0
        visit=defaultdict(list)

        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node==n:
                    if count:
                        return currTime
                    count+=1
                for nei in graph[node]:
                    nei_times=visit[nei]
                    if len(nei_times)==0 or (len(nei_times)==1 and nei_times[0]!=currTime):
                        q.append(nei)
                        visit[nei].append(currTime)
                    
            if (currTime//change)%2==1:
                currTime+=change-(currTime%change)
            currTime+=time