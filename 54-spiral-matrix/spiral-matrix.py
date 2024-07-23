from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        res = []
        
        dirr = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        i = j = k = 0  # start at the top-left corner
        
        for _ in range(rows * cols):
            res.append(matrix[i][j])
            visited.add((i, j))
            ni, nj = i + dirr[k][0], j + dirr[k][1]
            
            if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
                i, j = ni, nj
            else:
                k = (k + 1) % 4  # change direction
                i += dirr[k][0]
                j += dirr[k][1]
        
        return res
