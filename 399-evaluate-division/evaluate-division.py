class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=defaultdict(list)

        for i in range(len(values)):
            num,den=equations[i]
            val=values[i]

            adj[num].append((den,val))
            adj[den].append((num,1/val))
        
        #list is built
        res=[]

        for num,den in queries:

            q=deque()
            q.append((num,1))
            visited=set()
            flag=0

            while q:
                curr_node,curr_cost=q.popleft()

                if curr_node in visited:
                    continue
                visited.add(curr_node)

                for nei,cost in adj[curr_node]:
                    if nei==den:
                        res.append(curr_cost*cost)
                        flag=1
                        break
                    if nei not in visited:
                        q.append((nei,curr_cost*cost))
                if flag==1:
                    break
            if flag==0:
                res.append(-1.0)
        return res