class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:


        def topo(edges):
            graph=defaultdict(list)
            in_degree=[0 for _ in range(k+1)]

            for i,j in edges:
                graph[i].append(j)
                in_degree[j]+=1
            
            q=deque()

            for node in range(1,k+1):
                if in_degree[node]==0:
                    q.append(node)
       
            res=[]
            print(q)
            while q:
                curr_node=q.popleft()
                res.append(curr_node)
                for nei in graph[curr_node]:
                    in_degree[nei]-=1
                    if in_degree[nei]==0:
                        q.append(nei)
            print(res)
            if len(res)==k:
                return res
            return []
        
        row_order=topo(rowConditions)
        col_order=topo(colConditions)
        
        if not row_order or not col_order:
            return []
        
        res=[[0]*k for _ in range(k)]

        val_row={n:i for i,n in enumerate(row_order)}
        val_col={n:i for i,n in enumerate(col_order)}

        for num in range(1,k+1):
            r,c=val_row[num],val_col[num]
            res[r][c]=num
        return res