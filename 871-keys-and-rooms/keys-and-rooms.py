class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph={}
        for i in range(len(rooms)):
            graph[i]=rooms[i]

        visited=[0]*len(rooms)

        q=deque()
        q.append(0)

        print(graph)

        while q:
            node=q.popleft()
            if visited[node]:
                continue
            visited[node]=1
            for nei in graph[node]:
                if not visited[nei]:
                    q.append(nei)

        return sum(visited)==len(rooms)