class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #transpose matrix and flip it
        #to transpose reverse i,j
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                matrix[i][j],matrix[i][len(matrix)-1-j]=matrix[i][len(matrix)-1-j],matrix[i][j]