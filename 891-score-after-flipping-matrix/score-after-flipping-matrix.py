class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        for i in range(rows):
            if grid[i][0]==0:
                self.flip(grid,i)
        
        for col in range(cols):
            count=0
            for row in range(rows):
                if grid[row][col]==0:
                    count+=1
            if count>(rows//2):
                self.flip_col(grid,col)
        
        res=0
        for row in range(rows):
            curr=0
            power=1
            for col in range(cols-1,-1,-1):
                curr+=grid[row][col]*power
                power=power*2
            res+=curr
        
        return res



    def flip(self,grid,row):
        for i in range(len(grid[0])):
            if grid[row][i]==0:
                grid[row][i]=1
            else:
                grid[row][i]=0

    def flip_col(self,grid,col):
        for i in range(len(grid)):
            if grid[i][col]==0:
                grid[i][col]=1
            else:
                grid[i][col]=0