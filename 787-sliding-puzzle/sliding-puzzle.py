class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 1 2 3 4 5 0
        dirr=[[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]

        start=""

        for i in range(len(board)):
            for j in range(len(board[0])):
                start+=str(board[i][j])

        visited={}
        def swap(s,i,j):
            if i>j:
                i,j=j,i
            return s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
        def dfs(s,zero_pos,count):
            if s in visited and visited[s]<=count:
                return 
            visited[s]=count
            for next_pos in dirr[zero_pos]:
                dfs(swap(s,zero_pos,next_pos),next_pos,count+1)
        dfs(start,start.index("0"),0)
        return visited.get("123450",-1)

            