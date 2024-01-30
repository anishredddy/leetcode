class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def helper(i,j):
            nonlocal matrix
            for x in range(len(matrix)):
                matrix[x][j]=0
            for y in range(len(matrix[0])):
                matrix[i][y]=0
        stack=[]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if(matrix[row][col]==0):
                    stack.append([row,col])
        while stack:
            i,j=stack.pop()
            helper(i,j)
        return matrix

                