class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        order=len(matrix)
        left, right = 0,len(matrix[0])- 1
        n=-1
        for i in range(order):
            if(target>=matrix[i][0]):
                n=i
            else:
                break
        while left <= right:
            mid = left + (right - left) // 2
        
            if matrix[n][mid] == target:
                return True
            elif matrix[n][mid] < target:
                left = mid + 1 
            else:
                right = mid - 1
        return False