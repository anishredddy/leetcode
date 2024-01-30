class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        res=[[1],[1,1]]
        for i in range(2,numRows):
            curr=[1]
            for j in range(len(res[i-1])-1):
                curr.append(res[i-1][j]+res[i-1][j+1])
            curr.append(1)
            res.append(curr)
        return res
        