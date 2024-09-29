class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]!='1': continue
                dp[i][j]=max( dp[i][j], 1+min([dp[i-1][j],dp[i][j-1],dp[i-1][j-1]]) )
        return max(sum(dp,[]))**2