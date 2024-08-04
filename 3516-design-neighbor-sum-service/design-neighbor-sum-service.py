class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid=grid
        

    def adjacentSum(self, value: int) -> int:
        r,c=0,0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j]==value:
                    r,c=i,j
                    break
        dirr=[[1,0],[0,1],[-1,0],[0,-1]]

        res=0

        for x,y in dirr:
            if r+x in range(len(self.grid)) and c+y in range(len(self.grid[0])):
                res+=self.grid[r+x][c+y]
        return res

    def diagonalSum(self, value: int) -> int:
        r,c=0,0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j]==value:
                    r,c=i,j
                    break
        dirr=[[1,1],[-1,1],[-1,-1],[1,-1]]

        res=0

        for x,y in dirr:
            if r+x in range(len(self.grid)) and c+y in range(len(self.grid[0])):
                res+=self.grid[r+x][c+y]
        return res
        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)